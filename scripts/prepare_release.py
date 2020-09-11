"""
TODO:

# For each package:
- Check languages that have complete translation coverage
- Move major.minor.patch.dev0 to major.minor.patch with `bumpversion release`
- Move major.minor.patch to major.minor+1.patch with `bumpversion minor`
- `check-manifest -v`
- `python setup.py sdist bdist_wheel`
- `python -m twine check dist/*`
- `python -m twine upload dist/*`
"""
