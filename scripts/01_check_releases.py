# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""
# Get the latest tags of all the
# packages and update the repository-map.yml
"""
import argparse
import re
from pathlib import Path

import semantic_version as semver
import yaml
from packaging.version import parse

from github_ql import get_tags


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
        
    errors = []  # Will gather the list of extensions not matching the supported versions range
    
    for package_name in packages:
        current_version = parse(data[package_name]["current-version-tag"])
        if current_version.release is None:
            print(f"Package `{package_name}` has an unsupported version `{current_version.public}` - it will be skipped.")
            continue
        else:
            print(f"Looking for new releases for package `{package_name}`...")
            
        versions_range = data[package_name].get("supported-versions")
        if versions_range is not None:
            versions_range = semver.NpmSpec(versions_range)

        # Get the latest tags - assuming the repository is on github
        match = REPO_REGEX.match(data[package_name]["url"])
        if match is not None:
            repo = match.groupdict()

            try:
                tags = get_tags(repo["owner"], repo["repo"])
            except ValueError as err:
                print(f"Error when retrieving version for package `{package_name}`.")
                print(err)
                errors.append(str(err))
            else:
                for tag in tags:
                    version = parse(tag)
                    if version.release is None:
                        continue

                    if not version.is_devrelease and not version.is_prerelease and version > current_version:
                        print(f"Package `{package_name}` has a new version available: {version!s}.")
                        data[package_name]["current-version-tag"] = tag
                        if versions_range is not None and semver.Version(version.base_version) not in versions_range:
                            msg = "New version '{version}' is out of supported range '{range}'".format(
                                version=tag, range=data[package_name]["supported-versions"]
                            )
                            print(msg)
                            errors.append(msg)
                        break
                    elif version <= current_version:
                        break

    if len(errors) > 0:
        raise ValueError("\n".join(errors))

    (REPO_ROOT / REPO_MAP_FILE).write_text(yaml.safe_dump(data))
