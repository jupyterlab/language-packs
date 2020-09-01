# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
 
from setuptools import setup


setup(
    name="jupyterlab_language_pack_zh_CN",
    version="0.1.0",
    url="https://github.com/goanpeca/jupyterlab-language-packs",
    description="Jupyterlab Chinese (Simplified, China) Language Pack",
    install_requires=[],
    packages=[
        "jupyterlab_language_pack_zh_CN",
        "jupyterlab_language_pack_zh_CN.extensions",
    ],
    package_dir={
        "jupyterlab_language_pack_zh_CN": "jupyterlab_language_pack_zh_CN",
        "jupyterlab_language_pack_zh_CN.extensions": "jupyterlab_language_pack_zh_CN/extensions",
    },
    package_data={
        "jupyterlab_language_pack_zh_CN": ["*.json", "*.mo"],
        "jupyterlab_language_pack_zh_CN.extensions": ["*.json", "*.mo",],
    },
    entry_points={
        "jupyterlab.languagepack": ["zh_CN = jupyterlab_language_pack_zh_CN",]
    },
)
