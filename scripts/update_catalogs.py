"""
This script will update the catalogs using the information from the
`repository-map.yml` file.
"""

# Standard library imports
import os
import subprocess
import sys

# Third party imports
import yaml
import jupyterlab_translate.api as api

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = os.path.dirname(HERE)
REPOSITORIES_FOLDER = "repos"
LANGUAGE_PACKS_FOLDER = "language-packs"
REPO_MAP_FILE = "repository-map.yml"


def load_repo_map():
    """
    Load yaml file with mapping of package names to repo url and version.
    """
    fpath = os.path.join(REPO_ROOT, REPO_MAP_FILE)
    with open(fpath, "r") as fh:
        data = yaml.safe_load(fh.read())

    return data


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
    package_repo_dir = os.path.join(REPO_ROOT, REPOSITORIES_FOLDER, package_name)
    api.extract_language_pack(package_repo_dir, REPO_ROOT, package_name)


if __name__ == "__main__":
    args = sys.argv[1:]
    data = load_repo_map()
    packages = []

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
