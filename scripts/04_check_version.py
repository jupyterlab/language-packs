# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""
This script will check that all language pack have the same version
"""

import subprocess
import sys
from pathlib import Path

# Constants
HERE = Path(__file__).parent.resolve()
REPO_ROOT = HERE.parent
LANG_PACKS_PATH = REPO_ROOT / "language-packs"

if __name__ == "__main__":
    version = None
    errors = []
    for pkg_path in sorted(LANG_PACKS_PATH.iterdir()):
        if pkg_path.is_dir():
            hatch_error = None
            try:
                pkg_version = subprocess.check_output(
                    [sys.executable, "-m", "hatch", "version"],
                    cwd=pkg_path,
                    encoding="utf-8",
                    stderr=subprocess.PIPE,
                )
            except subprocess.CalledProcessError as e:
                last_line = e.stderr.splitlines()[-1]
                error_class, _, msg = last_line.partition(":")
                hatch_error = msg.strip()

            if version is None:
                print(f"Reference version taken from {pkg_path.name}: {pkg_version}.")
                version = pkg_version

            if hatch_error or pkg_version != version:
                errors.append((pkg_path.name, pkg_version, hatch_error))

    if errors:
        print("Following packages have singular versions:")
        print("Package name\t\t\tPkg version\tHatch error")
        for error in errors:
            print(f"{error[0]}\t{error[1]}\t{error[2]}")
        raise ValueError("Language packages do not have homogeneous version.")
