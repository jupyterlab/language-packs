# Release

The process below describes the procedure for JupyterLab package, but the same applies
for JupyterLab extensions.

## Update Catalogs

The first step when preparing a release is to make sure a beta or release candidate for JupyterLab
exists which should mean no new strings are expected to change in the code base.

Update the current catalog for JupyterLab and JupyterLab extensions.

## Wait for translations

Give some time to authors to update the new translations in the version.

## Merge pull request

Crowdin integration is currently set with the [JupyterLab-Bot](https://github.com/jupyterlab-bot).

Before merging the PR make sure to squash to a single commit.

If there are conflicts in the PR, close it and delete the branch, and wait for a new one
to be regenerated, which should be conflict free.

## Prepare packages

Run the `prepare_release.py` script to check which packages have 100% translation and bumb versions
accordingly. This script will print some information, bump package version and add commits and tags.

## Push commits and tags

Assuming there is a remote pointing to the upstream repository called repository, run:

```bash
git push upstream --tags
git push upstream master
```

This will trigger Github workflows on CI and make the corresponding releases and publication to
PyPI for the created tags.
