"""Extract the version from the bumpversion configuration."""

import configparser
import os
from pathlib import Path

# Constants
HERE = Path(__file__).parent.resolve()
REPO_ROOT = HERE.parent.parent
LANG_PACKS_PATH = REPO_ROOT / "language-packs"
BUMP_CONFIG = ".bumpversion.cfg"

if __name__ == "__main__":
    current_locale = os.environ.get("CURRENT_LOCALE")
    config_path  = LANG_PACKS_PATH / f"jupyterlab-language-pack-{current_locale}" / BUMP_CONFIG
    config = configparser.ConfigParser()
    config.read(config_path)

    print(config.get("bumpversion", "current_version"))
