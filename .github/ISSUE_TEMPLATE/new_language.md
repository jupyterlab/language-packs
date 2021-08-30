---
name: "\U0001F680 New Language Request"
about: Suggest a new new language
labels: enhancement
---

<!-- Welcome! Thank you for contributing. These HTML comments will not render in the issue, but you can delete them once you've read them if you prefer! -->

New language needs to add: <!--Add here the new language you want to be added -->
Language locale (optional): <!--Add here the locale for that language -->

## Checklist

Actions to be carry out in that order

- [ ] The language is available on [crowdin.com](https://crowdin.com/project/jupyterlab)
- [ ] The workflow `Prepare language packs for release` has been executed and the associated PR has been merged.
- [ ] Manually upload the Python package on PyPI
- [ ] Update the owners on PyPI to add jupyterlab-bot as maintainer
- [ ] Acknowledge the grant for the bot
- [ ] Update the [github action list](https://github.com/jupyterlab/language-packs/blob/814ee5589fd83ceaeb6ecaefa8ad2db741f3a2df/.github/workflows/release_publish.yml#L42)
- [ ] Update the [conda-forge variant list](https://github.com/conda-forge/jupyterlab-language-packs-feedstock/blob/master/recipe/conda_build_config.yaml)
