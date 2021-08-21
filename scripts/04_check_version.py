# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""
This script will check that all language pack have the same version
"""

import configparser
from pathlib import Path

# Constants
HERE = Path(__file__).parent.resolve()
REPO_ROOT = HERE.parent
LANG_PACKS_PATH = REPO_ROOT / "language-packs"
BUMP_CONFIG = ".bumpversion.cfg"

if __name__ == "__main__":
    version = None
    errors = []
    for config_path in sorted(LANG_PACKS_PATH.rglob(BUMP_CONFIG)):
        if config_path.is_file():
            config = configparser.ConfigParser()
            config.read(config_path)

            pkg_version = config.get("bumpversion", "current_version")
            if version is None:
                print(
                    f"Reference version taken from {config_path.parent.name}: {pkg_version}."
                )
                version = pkg_version
            elif pkg_version != version:
                errors.append((config_path.parent.name, pkg_version, version))

    if errors:
        print("Following packages have singular versions:")
        print("Package name\t\tPkg version\tCommon version")
        for error in errors:
            print(f"{error[0]}\t{error[1]}\t{error[2]}")
        raise ValueError("Language packages do not have homogeneous version.")
