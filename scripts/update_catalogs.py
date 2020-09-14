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
import os
import subprocess
import sys

# Third party imports
import jupyterlab_translate.api as api
import yaml

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = os.path.dirname(HERE)
REPOSITORIES_FOLDER = "repos"
LANGUAGE_PACKS_FOLDER = "language-packs"
REPO_MAP_FILE = "repository-map.yml"
CROWDIN_FILE = "crowdin.yml"


def load_repo_map():
    """
    Load yaml file with mapping of package names to repo url and version.
    """
    fpath = os.path.join(REPO_ROOT, REPO_MAP_FILE)
    with open(fpath, "r") as fh:
        data = yaml.safe_load(fh.read())

    return data


def save_crowdin(data):
    """
    Save crowdin `data`.
    """
    fpath = os.path.join(REPO_ROOT, CROWDIN_FILE)
    with open(fpath, "w") as fh:
        fh.write(yaml.safe_dump(data))


def load_crowdin():
    """
    Load crowdin data.
    """
    fpath = os.path.join(REPO_ROOT, CROWDIN_FILE)
    with open(fpath, "r") as fh:
        data = yaml.safe_load(fh.read())

    return data


def update_crowdin_config():
    """
    Update crowdin configuration to match `reposiory-map.yml`.
    """
    data = load_repo_map()
    crowdin_data = load_crowdin()
    files = crowdin_data["files"]
    packages = [
        {
            "source": "/jupyterlab/locale/jupyterab.pot",
            "traslation": (
                f"/jupyterlab/locale/%locale_with_underscore%"
                f"/LC_MESSAGES/%file_name%.po"
            ),
        }
    ]
    for pkg_name in sorted(data):
        if pkg_name != "jupyterlab":
            pkg_name_norm = pkg_name.replace("-", "_")
            packages.append({
                "source": f"/extensions/{pkg_name}/locale/{pkg_name_norm}.pot",
                "translation": (
                    f"/extensions/{pkg_name}/locale"
                    f"/%locale_with_underscore%/LC_MESSAGES/%file_name%.po"
                ),
            })

    crowdin_data["files"] = packages
    save_crowdin(crowdin_data)


def update_repo(package_name, url, version):
    """
    Clone or update repo for given package and checkout `version` reference.
    """
    repos_path = os.path.join(REPO_ROOT, REPOSITORIES_FOLDER)
    clone_path = os.path.join(repos_path, package_name)

    if not os.path.isdir(clone_path):
        args = ["git", "clone", url + ".git", package_name]
        p = subprocess.Popen(args, cwd=repos_path)
        p.communicate()
    else:
        args = ["git", "fetch", "origin"]
        p = subprocess.Popen(args, cwd=repos_path)
        p.communicate()

    args = ["git", "checkout", version]
    p = subprocess.Popen(args, cwd=clone_path)
    p.communicate()


def update_catalog(package_name, version):
    """
    Create or update pot catalogs for package_name and version using
    `jupyterlab-translate`.
    """
    package_repo_dir = os.path.join(REPO_ROOT, REPOSITORIES_FOLDER, package_name)
    api.extract_language_pack(package_repo_dir, REPO_ROOT, package_name)


if __name__ == "__main__":
    args = sys.argv[1:]
    data = load_repo_map()
    packages = []

    # Ensure repository map and crowdin config are in sync
    update_crowdin_config()

    if len(args) == 1:
        package_name = args[0]
        # Update package if found in the repository-map.yml
        if package_name in data:
            packages = [package_name]
    elif len(args) == 0:
        packages = sorted(data.keys())
    else:
        sys.exit(0)
    
    for package_name in packages:
        url = data[package_name]["url"]
        version = data[package_name]["current-version-tag"]
        update_repo(package_name, url, version)
        update_catalog(package_name, version)
