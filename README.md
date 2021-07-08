# Jupyterlab Language Packs

[![Crowdin](https://badges.crowdin.net/jupyterlab/localized.svg)](https://crowdin.com/project/jupyterlab)

Jupyterlab language packs.

## Install

To install a specific language pack please see the [available packs](https://github.com/jupyterlab/language-packs/tree/master/language-packs).

## Adding a new extension

Follow the instructions described in the [developer documentation](https://jupyterlab.readthedocs.io/en/stable/) of JupyterLab.

Create a PR adding a new entry to the [repository-map.yml](https://github.com/jupyterlab/language-packs/blob/master/repository-map.yml) file.

```yaml
# Package name, repository url and current version
jupyterlab:
  current-version-tag: v3.0.0b4
  url: https://github.com/jupyterlab/jupyterlab
# Add extensions alphabetically. Use lowercase for keys.
dask-labextension:
  current-version-tag: v1.0.0
  url: https://github.com/dask/dask-labextension
jupyterlab-git:
  current-version-tag: v0.21.1
  url: https://github.com/jupyterlab/jupyterlab-git
```

After the PR is merged, our bot will create/update the `.pot` files in a subsequent PR. Once merged, the catalog for the new extension will be available on [Crowdin](https://crowdin.com/project/jupyterlab).

When translations are completed for a given set of packages a new language pack for the given language will be released as python packages via [PyPI](https://pypi.org/) and conda packages via [conda-forge](https://conda-forge.org/).

## Contributing

Please visit [Crowdin](https://crowdin.com/project/jupyterlab) to contribute to a language pack.
