# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Standard library imports
import ast
import os

# Third party imports
from setuptools import find_packages, setup

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))


def get_version(module="jupyterlab_language_pack_zh_CN"):
    """Get version."""
    with open(os.path.join(HERE, module, "__init__.py"), "r") as f:
        data = f.read()

    lines = data.split("\n")
    for line in lines:
        if line.startswith("__version__"):
            version = ast.literal_eval(line.split("=")[-1].strip())
            break

    return version


def get_description():
    """Get long description."""
    with open(os.path.join(HERE, "README.md"), "r") as f:
        data = f.read()

    return data


setup(
    name="jupyterlab-language-pack-zh-CN",
    version=get_version(),
    description="Jupyterlab Chinese (Simplified, China) Language Pack",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    keywords=["jupyterlab", "language", "language pack", "localization"],
    url="https://github.com/jupyterlab/language-packs",
    author="Project Jupyter Contributors",
    author_email="jupyter@googlegroups.com",
    license="BSD-3-Clause",
    platforms="Linux, Mac OS X, Windows",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "jupyterlab.languagepack": ["zh_CN = jupyterlab_language_pack_zh_CN"]
    },
)
