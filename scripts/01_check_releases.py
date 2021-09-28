# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""
# Get the latest tags of all the
# packages and update the repository-map.yml
"""
import argparse
import re
import requests
from pathlib import Path

import yaml
from packaging.version import parse

# Constants
HERE = Path(__file__).parent.resolve()
REPO_ROOT = HERE.parent
REPO_MAP_FILE = "repository-map.yml"
REPO_REGEX = re.compile(r"^https://(www)?github\.com/(?P<owner>.+)/(?P<repo>.+)(\.git)?$")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update repositories to latest tag.")
    parser.add_argument("packages", nargs="*", help="Package to test for update")
    
    args = parser.parse_args()

    data = yaml.safe_load((REPO_ROOT / REPO_MAP_FILE).read_text())
    
    if len(args.packages) == 0:
        packages = sorted(data.keys())
    else:
        packages = [pkg for pkg in args.packages if pkg in data]
    
    with requests.Session() as s:
        for package_name in packages:
            current_version = parse(data[package_name]["current-version-tag"])
            if current_version.release is None:
                print(f"Package `{package_name}` has an unsupported version `{current_version.public}` - it will be skipped.")
                continue

            # Get the latest tags - assuming the repository is on github
            match = REPO_REGEX.match(data[package_name]["url"])
            if match is not None:
                repo = match.groupdict()

                response = s.get(
                    "https://api.github.com/repos/{owner}/{repo}/tags".format(**repo),
                    headers={"Accept": "application/vnd.github.v3+json"}
                )

                if response.ok:
                    for tag in response.json():
                        version = parse(tag["name"])
                        if not version.is_prerelease and version > current_version:
                            print(f"Package `{package_name}` has a new version available: {version!s}.")
                            data[package_name]["current-version-tag"] = tag["name"]
                            break
                        elif version <= current_version:
                            break

    (REPO_ROOT / REPO_MAP_FILE).write_text(yaml.safe_dump(data))
