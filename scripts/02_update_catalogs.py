# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""
This script will update the catalogs using the information from the
`repository-map.yml` file.

This script will:
- Check `repository-map.yml` urls are valid.
- Update the crowdin.yml to match `repository-map.yml`
- Clone repos or fetch from origin  based on information from `repository-map.yml`
- Checkout the current version
- Create a `gettext` catalog (*.pot) or update an existing catalog using
  `jupyterlab-translate`
"""

# Standard library imports
import argparse
import re
import subprocess
import time
from pathlib import Path

# Third party imports
import jupyterlab_translate.api as api
import semantic_version as semver
import yaml
from packaging.version import parse

from github_ql import get_tags

# Constants
HERE = Path(__file__).parent.resolve()
REPO_ROOT = HERE.parent
REPOSITORIES_FOLDER = "repos"
LANGUAGE_PACKS_FOLDER = "language-packs"
REPO_MAP_FILE = "repository-map.yml"
CROWDIN_FILE = "crowdin.yml"
REPO_REGEX = re.compile(r"^https://(www)?github\.com/(?P<owner>.+)/(?P<repo>.+)(\.git)?$")


def load_repo_map() -> dict:
    """
    Load yaml file with mapping of package names to repo url and version.
    """
    fpath = REPO_ROOT / REPO_MAP_FILE

    return yaml.safe_load(fpath.read_text())


def save_crowdin(data: dict) -> None:
    """
    Save crowdin `data`.
    """
    fpath = REPO_ROOT / CROWDIN_FILE
    fpath.write_text(yaml.safe_dump(data))


def load_crowdin() -> dict:
    """
    Load crowdin data.
    """
    fpath = REPO_ROOT / CROWDIN_FILE

    return yaml.safe_load(fpath.read_text())


def update_crowdin_config():
    """
    Update crowdin configuration to match `repository-map.yml`.
    """
    data = load_repo_map()
    crowdin_data = load_crowdin()
    # _files = crowdin_data["files"]
    packages = [
        {
            "source": "/jupyterlab/locale/jupyterlab.pot",
            "translation": (
                f"/jupyterlab/locale/%locale_with_underscore%"
                f"/LC_MESSAGES/%file_name%.po"
            ),
        }
    ]
    for pkg_name in sorted(data):
        if pkg_name != "jupyterlab":
            pkg_name_norm = pkg_name.replace("-", "_")
            packages.append(
                {
                    "source": f"/extensions/{pkg_name_norm}/locale/{pkg_name_norm}.pot",
                    "translation": (
                        f"/extensions/{pkg_name_norm}/locale"
                        f"/%locale_with_underscore%/LC_MESSAGES/%file_name%.po"
                    ),
                }
            )

    crowdin_data["files"] = packages
    save_crowdin(crowdin_data)


def update_repo(package_name: str, url: str, version: str):
    """
    Clone or update repo for given package and checkout `version` reference.
    """
    repos_path = REPO_ROOT / REPOSITORIES_FOLDER
    clone_path = repos_path / package_name
    repos_path.mkdir(parents=True, exist_ok=True)

    if not clone_path.is_dir():
        args = ["git", "clone", "--depth=1", f"--branch={version}", f"{url}.git", package_name]
        subprocess.check_call(args, cwd=repos_path)

    is_branch = False
    try:
        args = ["git", "fetch", "--depth=1", "origin", f"+refs/tags/{version}:refs/tags/{version}"]
        subprocess.check_call(args, cwd=clone_path)
    except subprocess.CalledProcessError as err:
        # The version is probably a branch
        args = ["git", "fetch", "--depth=1", "origin", f"+refs/heads/{version}:refs/remotes/origin/{version}"]
        subprocess.check_call(args, cwd=clone_path)
        is_branch = True

    args = ["git", "checkout", version]
    subprocess.check_call(args, cwd=clone_path)

    if is_branch:
        args = ["git", "pull", "origin", version]
        subprocess.check_call(args, cwd=clone_path)


def update_catalog(package_name: str, version: str, merge: bool):
    """
    Create or update pot catalogs for package_name and version using
    `jupyterlab-translate`.

    TODO: version is ignored
    """
    package_repo_dir = REPO_ROOT / REPOSITORIES_FOLDER / package_name
    api.extract_language_pack(package_repo_dir, REPO_ROOT, package_name, merge)

def get_min(clause):
    """Extract the smallest version from a NpmSpec range."""
    if isinstance(clause, semver.base.AllOf):
        return min(map(lambda c: get_min(c), clause))
    elif isinstance(clause, semver.base.AnyOf):
        return min(map(lambda c: get_min(c), clause.clauses))
    elif isinstance(clause, semver.base.Range):
        return clause.target

if __name__ == "__main__":
    start_run_time = time.time()
    parser = argparse.ArgumentParser(description="Update JupyterLab language packages source strings.")
    parser.add_argument("packages", nargs="*", help="Package to update")

    args = parser.parse_args()

    data = load_repo_map()

    # Ensure repository map and crowdin config are in sync
    update_crowdin_config()

    if len(args.packages) == 0:
        packages = sorted(data.keys())
    else:
        packages = [pkg for pkg in args.packages if pkg in data]

    for package_name in packages:
        print(f'\n\nUpdating catalog for "{package_name}"\n\n')
        url = data[package_name]["url"]
        current_version = data[package_name]["current-version-tag"]
        cur_version = parse(current_version)
        should_merge = False

        # Get the latest tags - assuming the repository is on github
        match = REPO_REGEX.match(data[package_name]["url"])
        if data[package_name].get("supported-versions") is not None and match is not None:
            repo = match.groupdict()
            range = semver.NpmSpec(data[package_name]["supported-versions"])
            # min_version = get_min(range.clause)  # Not use

            # For JupyterLab we filter explicitly to catch version belonging to minor range
            ref_filter = f"v{cur_version.major}.{cur_version.minor}" if package_name == "jupyterlab" else None
            try:
                # Request 100 tags in descending commit date order
                tags = get_tags(repo["owner"], repo["repo"], filter=ref_filter)
            except ValueError as err:
                print(f"Error when retrieving version for package `{package_name}`.")
                print(err)
            else:
                for tag in tags:
                    version = parse(tag)
                    if (
                        version.release is None  # non standard version
                        or version == cur_version  # Handle as last step
                        or version.is_devrelease # Skip non final versions
                        or version.is_prerelease
                    ):
                        continue

                    # The following will erase any part of the version that is not (major, minor, patch)
                    semversion = semver.Version(version.base_version)

                    if semversion in range:
                        print(f"\nMerge version {version!s} for `{package_name}`.\n")
                        update_repo(package_name, url, tag)
                        update_catalog(package_name, current_version, should_merge)
                        should_merge = True

                    # This allows to break when the version is below the supported range. But it breaks merging tags if newer security release
                    # on older versions are carried out like for JupyterLab --> We scan for all first 100 tags
                    # elif semversion < min_version:
                    #     print(f"\nNext available version {semversion!s} for `{package_name}` is below the supported range {range!s}.\n")
                    #     break
        
        # The final step is to merge the current version so the POT file is tagged accordingly
        update_repo(package_name, url, current_version)
        update_catalog(package_name, current_version, should_merge)

    delta = round(time.time() - start_run_time, 0)
    print(f"\n\n\nCatalogs updated in {delta} seconds\n")
