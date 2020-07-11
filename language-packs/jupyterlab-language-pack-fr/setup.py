from setuptools import setup


setup(
    name="jupyterlab_language_pack_fr",
    version="0.1.0",
    url="https://github.com/goanpeca/jupyterlab-language-packs",
    description="Jupyterlab French Language Pack",
    install_requires=[],
    packages=[
        "jupyterlab_language_pack_fr",
        "jupyterlab_language_pack_fr.extensions",
    ],
    package_dir={
        "jupyterlab_language_pack_fr": "jupyterlab_language_pack_fr",
        "jupyterlab_language_pack_fr.extensions": "jupyterlab_language_pack_fr/extensions",
    },
    package_data={
        "jupyterlab_language_pack_fr": ["*.json", "*.mo"],
        "jupyterlab_language_pack_fr.extensions": ["*.json", "*.mo",],
    },
    entry_points={
        "jupyterlab.languagepack": ["fr = jupyterlab_language_pack_fr",]
    },
)
