"""
TODO:

# For each package:
- Check languages that have complete translation coverage
- Move major.minor.patch.dev0 to major.minor.patch with `bumpversion release`
- Move major.minor.patch to major.minor+1.patch with `bumpversion minor`
- `check-manifest -v`
- `python setup.py sdist bdist_wheel`
- `python -m twine check dist/*`
- `python -m twine upload dist/*`
"""

# Standard library imports
import os

# Third party imports
import polib
from jupyterlab_translate import api

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = os.path.dirname(HERE)
LANG_PACKS_DIR = os.path.join(REPO_ROOT, "language-packs")
JLAB_LOCALE_DIR = os.path.join(REPO_ROOT, "jupyterlab", "locale")
JLAB_EXT_DIR = os.path.join(REPO_ROOT, "jupyterlab_extensions")
LC_MESSAGES_FOLDER = "LC_MESSAGES"


def prepare_jupyterlab_lp_release():
    """
    """
    for locale in os.listdir(JLAB_LOCALE_DIR):
        if os.path.isdir(os.path.join(JLAB_LOCALE_DIR, locale)):
            po_dir = os.path.join(JLAB_LOCALE_DIR, locale, LC_MESSAGES_FOLDER)
            for fname in os.listdir(po_dir):
                if fname.endswith(".po"):
                    po_file_path = os.path.join(po_dir, fname)
                    po = polib.pofile(po_file_path)
                    percent_translated = po.percent_translated()
                    if percent_translated == 100:
                        print(locale, f"{percent_translated}%", "compiling...")
                        api.compile_language_pack(REPO_ROOT, "jupyterlab", [locale])
                        break
                    else:
                        print(locale, f"{percent_translated}%")


def prepare_jupyterlab_ext_lp_release():
    pass


if __name__ == "__main__":
    prepare_jupyterlab_lp_release()
