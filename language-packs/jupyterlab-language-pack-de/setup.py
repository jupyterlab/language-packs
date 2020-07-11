from setuptools import setup


setup(
    name="jupyterlab_language_pack_de",
    version="0.1.0",
    url="https://github.com/goanpeca/jupyterlab-language-packs",
    description="Jupyterlab German Language Pack",
    install_requires=[],
    packages=[
        "jupyterlab_language_pack_de",
        "jupyterlab_language_pack_de.extensions",
    ],
    package_dir={
        "jupyterlab_language_pack_de": "jupyterlab_language_pack_de",
        "jupyterlab_language_pack_de.extensions": "jupyterlab_language_pack_de/extensions",
    },
    package_data={
        "jupyterlab_language_pack_de": ["*.json", "*.mo"],
        "jupyterlab_language_pack_de.extensions": ["*.json", "*.mo",],
    },
    entry_points={
        "jupyterlab.languagepack": ["de = jupyterlab_language_pack_de",]
    },
)
