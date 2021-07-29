# Release

The process below describes the procedure for JupyterLab package, but the same applies
for JupyterLab extensions.

## Environment

Create an environment with the dependencies on `requirements/release.txt`.

```bash
conda create -n language-packs nodejs python -c conda-forge -y -q
conda activate language-packs
pip install -r requirements/release.txt
```

Also make sure you have `gettext-extract` available globally from NPM.

```bash
npm install gettext-extract -g
```

## Update Catalogs

The first step when preparing a release is to make sure a beta or release candidate for JupyterLab
exists which should mean no new strings are expected to change in the code base.

With this information update the `repository-map.yml` file to point to the latest version for
which translation strings are going to be scrapped from the codebase.

Update the current catalog for JupyterLab and JupyterLab extensions.

```python
python scripts/02_update_catalogs.py
```

Push the changes to Github, Crowdin will update the loaded catalogs and expose and new strings to
translators.

## Wait for translations

Give some time to authors to update the new translations in the version.

## Merge pull request

Crowdin integration is currently set with the [JupyterLab-Bot](https://github.com/jupyterlab-bot).

Before merging the PR make sure to squash to a single commit to keep git history clean.

If there are conflicts in the PR, close it and delete the branch, and wait for a new one
to be regenerated, which should be conflict free.

## Prepare packages

Run the `05_prepare_release.py` script to check which packages have 100% translation and bump versions
accordingly. This script will print some information, bump package versions and add commits and tags.

## Push commits and tags

Assuming there is a remote pointing to the upstream repository called `upstream`, run:

```bash
git push upstream --tags
git push upstream master
```

This will trigger Github workflows on CI and make the corresponding releases on Github and PyPI.
