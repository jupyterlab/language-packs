# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""
This script will prepare a release by:
- Update the contributors list
- Bumping the version
"""

# Standard library imports
import argparse
import os
import re
import subprocess
import sys
import traceback
from pathlib import Path
from typing import Optional

# Third party imports
from jupyterlab_translate import api, contributors


# Constants
HERE = Path(__file__).parent.resolve()
REPO_ROOT = HERE.parent
LANG_PACKS_PATH = REPO_ROOT / "language-packs"
PYPROJECT_FILE = "pyproject.toml"
VERSION_REGEX = re.compile(r"\d+\.\d+\.post\d+")


def bumpversion(path: Path, new_version: Optional[str] = "rev") -> None:
    """Update the package version.

    Args:
        path: Package path
        release: Is the new version a release or a patch version.
    """
    subprocess.check_call(["hatch", "version", new_version], cwd=path)


def prepare_jupyterlab_lp_release(
    crowdin_key: str, new_version: Optional[str] = "rev"
) -> None:
    """Prepare the JupyterLab Language Packages release

    Version are in format X.Y.postZ and by default Z will be bumped.

    Args:
        crowding_key: Crowdin API key
        new_version: [optional] New version of the package - default "rev"
    """
    # This assumes the JupyterLab folder is the source of truth for available locales
    for package_dir in sorted(filter(lambda i: i.is_dir(), LANG_PACKS_PATH.iterdir())):
        print(f"Prepare release for {package_dir.name}")
        locale_name = package_dir.name[-5:]
        locale = locale_name.replace("-", "_")

        # Bump the version
        if (package_dir / PYPROJECT_FILE).exists():
            try:
                subprocess.check_call(
                    [
                        sys.executable,
                        "-m",
                        "copier",
                        "--force",
                        "--vcs-ref",
                        "HEAD",
                        "update",
                    ],
                    cwd=package_dir,
                )
            except subprocess.CalledProcessError:
                print(f"Failed to update the package template for {package_dir.name}.")
                traceback.print_exc()

            bumpversion(package_dir, new_version)
        else:
            if VERSION_REGEX.fullmatch(new_version) is None:
                api.create_new_language_pack(LANG_PACKS_PATH, locale)
            else:
                api.create_new_language_pack(
                    LANG_PACKS_PATH,
                    locale,
                    version=new_version,
                )

        try:
            # Update the contributors file
            contributors_file = package_dir / contributors.CONTRIBUTORS
            contributors_file.write_text(
                contributors.get_contributors_report(
                    locale=locale_name, crowdin_key=crowdin_key
                )
            )

        except BaseException:
            print(
                f"An error occurred when generating the contributors list for '{locale_name}'."
            )
            traceback.print_exc()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prepare JupyterLab language packages for release"
    )
    parser.add_argument(
        "--new-version", default="rev", help="New version of the language packages"
    )
    parser.add_argument(
        "--crowdin-key",
        default=os.environ.get("CROWDIN_API_KEY"),
        help="Crowdin API key",
    )
    args = parser.parse_args()

    if args.crowdin_key is None:
        raise ValueError(
            "Crowdin API key needs to be set using either the "
            "'--crowdin-key' option or the 'CROWDIN_API_KEY' environment variable"
        )

    prepare_jupyterlab_lp_release(args.crowdin_key, args.new_version)
