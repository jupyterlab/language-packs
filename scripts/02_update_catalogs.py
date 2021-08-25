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
import os
import subprocess
import time
from pathlib import Path

# Third party imports
# import click
import jupyterlab_translate.api as api
import yaml

# Constants
HERE = Path(__file__).parent.resolve()
REPO_ROOT = HERE.parent
REPOSITORIES_FOLDER = "repos"
LANGUAGE_PACKS_FOLDER = "language-packs"
REPO_MAP_FILE = "repository-map.yml"
CROWDIN_FILE = "crowdin.yml"


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
        args = ["git", "clone", url + ".git", package_name]
        subprocess.check_call(args, cwd=repos_path)

    args = ["git", "fetch", "--tags"]
    subprocess.check_call(args, cwd=clone_path)

    args = ["git", "checkout", version]
    subprocess.check_call(args, cwd=clone_path)

    if version in ["master", "main"]:
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


if __name__ == "__main__":
    start_run_time = time.time()
    parser = argparse.ArgumentParser(description="Update JupyterLab language packages source strings.")
    parser.add_argument("packages", nargs="*", help="Package to update")
    parser.add_argument("--no-merge", action="store_true", help="If present, the existing PO template file will be overridden (by default the new strings are merged).")

    args = parser.parse_args()

    data = load_repo_map()
    
    # Ensure repository map and crowdin config are in sync
    update_crowdin_config()
    
    if len(args.packages) == 0:
        packages = sorted(data.keys())
    else:
        packages = [pkg for pkg in args.packages if pkg in data]
    
    merge = not args.no_merge and os.environ.get("NO_MERGE_POT", "false") == "false"

    for package_name in packages:
        print(f'\n\nUpdating catalog for "{package_name}" with {"" if merge else "no "}merge\n\n')
        url = data[package_name]["url"]
        version = data[package_name]["current-version-tag"]
        update_repo(package_name, url, version)
        update_catalog(package_name, version, merge)

    delta = round(time.time() - start_run_time, 0)
    print(f"\n\n\nCatalogs updated in {delta} seconds\n")
