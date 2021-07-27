# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""
"""

# Standard library imports
import configparser
import hashlib
import os
import pathlib

# Third party imports
import polib
import subprocess
import traceback
from cookiecutter.main import cookiecutter
from jupyterlab_translate import api

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = os.path.dirname(HERE)
LANG_PACKS_PATH = os.path.join(REPO_ROOT, "language-packs")
JLAB_LOCALE_PATH = os.path.join(REPO_ROOT, "jupyterlab", "locale")
JLAB_EXT_PATH = os.path.join(REPO_ROOT, "extensions")
LOCALE_FOLDER = "locale"
LC_MESSAGES_FOLDER = "LC_MESSAGES"
BUMP_CONFIG = ".bumpversion.cfg"


def load_hash(package_dir):
    """ """
    hash_value = None
    config_path = os.path.join(package_dir, BUMP_CONFIG)
    if os.path.isfile(config_path):
        config = configparser.ConfigParser()
        config.read(config_path)

        hash_value = config["hash"]["value"]
        if not hash_value:
            hash_value = None

    return hash_value


def save_hash(package_dir, hash_value):
    config_path = os.path.join(package_dir, BUMP_CONFIG)
    config = configparser.ConfigParser()

    if os.path.isfile(config_path):
        config.read(config_path)
        config["hash"]["value"] = hash_value
        with open(config_path, "w") as fh:
            config.write(fh)


def create_hash(po_file_path):
    hasher = hashlib.sha256()
    hasher.update(pathlib.Path(po_file_path).read_bytes())
    return hasher.hexdigest()


def is_updated_translation(po_file_path, package_dir, locale):
    """ """
    old_hash = load_hash(package_dir)

    if not os.path.isdir(package_dir):
        cookiecutter(
            "https://github.com/jupyterlab/language-pack-cookiecutter.git",
            no_input=True,
            extra_context={
                "locale": locale.replace("_", "-"),
                "locale_underscore": locale,
                "language": locale,
            },
            output_dir="language-packs",
        )

    new_hash = create_hash(po_file_path)

    if old_hash is None:
        return True
    else:
        return old_hash != new_hash


def bumbversion(path, release=False):
    if release:
        cmd_args = ["bump2version", "release", "--verbose", "--tag"]
    else:
        cmd_args = ["bump2version", "patch", "--verbose"]

    p = subprocess.Popen(cmd_args, cwd=path)
    p.communicate()


def prepare_jupyterlab_lp_release():
    """ """
    extensions = []
    for pkg_name in sorted(os.listdir(JLAB_EXT_PATH)):
        extension_path = os.path.join(JLAB_EXT_PATH, pkg_name)
        if os.path.isdir(extension_path):
            extensions.append(pkg_name)

    print(extensions)

    # return

    # TODO: Generalize for extensions
    for locale in sorted(os.listdir(JLAB_LOCALE_PATH)):
        if os.path.isdir(os.path.join(JLAB_LOCALE_PATH, locale)):
            try:
                po_dir = os.path.join(JLAB_LOCALE_PATH, locale, LC_MESSAGES_FOLDER)
                for fname in os.listdir(po_dir):
                    if fname.endswith(".po"):
                        po_file_path = os.path.join(po_dir, fname)
                        po = polib.pofile(po_file_path)
                        percent_translated = po.percent_translated()
                        locale_name = locale.replace("_", "-")
                        package_dir = os.path.join(
                            LANG_PACKS_PATH, f"jupyterlab-language-pack-{locale_name}"
                        )
                        if percent_translated >= 0:
                            if is_updated_translation(
                                po_file_path, package_dir, locale
                            ):
                                print(
                                    locale,
                                    f"{percent_translated}%",
                                    "compiling, commiting and tagging...",
                                )
                                api.compile_language_pack(
                                    REPO_ROOT, "jupyterlab", [locale]
                                )
                                save_hash(package_dir, create_hash(po_file_path))
                                # bumbversion(package_dir, release=True)
                                # bumbversion(package_dir, release=False)
                            else:
                                print(
                                    locale,
                                    f"{percent_translated}%",
                                    "package has not changed",
                                )

                            # TODO: Add a hash of the json file or similar to keep track if things change
                            # when something is already on 100%
                            # print(package_dir)
                            break
                        else:
                            print(locale, f"{percent_translated}%")
            except BaseException as err:
                print(f"An error occured when generating the language package {locale}")
                traceback.print_exc()


if __name__ == "__main__":
    prepare_jupyterlab_lp_release()
