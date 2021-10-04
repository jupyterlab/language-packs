# Jupyterlab Language Packs

[![Crowdin](https://badges.crowdin.net/jupyterlab/localized.svg)](https://crowdin.com/project/jupyterlab)

Jupyterlab language packs.

## Install

To install a specific language pack please see the [available packs](https://github.com/jupyterlab/language-packs/tree/master/language-packs).

## Adding a new extension

Follow the instructions described in the [developer documentation](https://jupyterlab.readthedocs.io/en/stable/extension/internationalization.html) of JupyterLab.

Create a PR adding a new entry to the [repository-map.yml](https://github.com/jupyterlab/language-packs/blob/master/repository-map.yml) file.

```yaml
# Packages in alphabetical order
dask-labextension:
  current-version-tag: 5.0.2
  supported-versions: 5.0.x
  url: https://github.com/dask/dask-labextension
jupyterlab:
  current-version-tag: v3.1.14
  supported-versions: 3.1.x
  url: https://github.com/jupyterlab/jupyterlab
jupyterlab-git:
  current-version-tag: v0.32.4
  supported-versions: '>=0.30.0 <0.40.0'
  url: https://github.com/jupyterlab/jupyterlab-git
```

The three entries required are:

- `current-version-tag`: The latest Git tag to consider as reference for the package.
- `supported-versions`: A semver range (npm syntax) of supported versions.
- `url`: Git repository URL (only HTTP on GitHub is supported).

The current tag is used by a bot to check for new GitHub release. If one is detected, it
will bump the tag and open a PR to add this change.

The source strings are gathered for multiple versions matching the `supported-versions` range.
The list of versions included is computed as follow:

1. Get the last 100 tags from the GitHub repository
2. Check if the tag is a parsable non-dev non-prerelease version (parsing is done using Python function `packaging.version.parse`)
3. Check that the tag is part of the supported range(s)

> The `current-version-tag` can be a _branch_ name (not recommended). In such a case, `supported-versions` has
> no effect and the source strings are only extracted from the current branch HEAD commit (no merging with the
> previous POT file).

After the PR is merged, our bot will create/update the `.pot` files in a subsequent PR. Once merged, the catalog for the new extension will be available on [Crowdin](https://crowdin.com/project/jupyterlab).

When translations are completed for a given set of packages a new language pack for the given language will be released as python packages via [PyPI](https://pypi.org/) and conda packages via [conda-forge](https://conda-forge.org/).

## Contributing

Please visit [Crowdin](https://crowdin.com/project/jupyterlab) to contribute to a language pack.
