from setuptools import setup

setup(
    name="jupyterlab_language_pack_es",
    version="0.1.0",
    url="https://github.com/goanpeca/jupyterlab-language-packs",
    description="Jupyterlab Spanish Language Pack",
    install_requires=[],
    packages=[
        "jupyterlab_language_pack_es",
        "jupyterlab_language_pack_es.extensions",
    ],
    package_dir={
        "jupyterlab_language_pack_es": "jupyterlab_language_pack_es",
        "jupyterlab_language_pack_es.extensions": "jupyterlab_language_pack_es/extensions",
    },
    package_data={
        "jupyterlab_language_pack_es": ["*.json", "*.mo"],
        "jupyterlab_language_pack_es.extensions": ["*.json", "*.mo",],
    },
    entry_points={
        "jupyterlab.languagepack": ["es = jupyterlab_language_pack_es",]
    },
)
