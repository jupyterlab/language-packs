# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""
This script will check that all language pack have the same version
"""

import configparser
import subprocess
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

            # Check version are consistent between package
            pkg_version = config.get("bumpversion", "current_version")
            if version is None:
                print(
                    f"Reference version taken from {config_path.parent.name}: {pkg_version}."
                )
                version = pkg_version

            # Check package version is coherent with bump2version configuration
            bumpversion_error = None
            try:
                subprocess.check_output(
                    ["bump2version", "--dry-run", "--allow-dirty", "build"],
                    stderr=subprocess.PIPE,
                    encoding="utf-8",
                    cwd=config_path.parent
                )
            except subprocess.CalledProcessError as e:
                last_line = e.stderr.splitlines()[-1]
                error_class, _, msg = last_line.partition(":")
                bumpversion_error = msg.strip()

            if bumpversion_error or pkg_version != version:
                errors.append((config_path.parent.name, pkg_version, bumpversion_error))

    if errors:
        print("Following packages have singular versions:")
        print("Package name\t\t\tPkg version\tBumpversion error")
        for error in errors:
            print(f"{error[0]}\t{error[1]}\t{error[2]}")
        raise ValueError("Language packages do not have homogeneous version.")
