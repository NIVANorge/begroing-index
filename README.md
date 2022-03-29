# Index calculation

This library provides functions for calculating data products that contribute towards reaching the goals of EU's water directive.

## Data products

Currently, the following index calculations are supported:

- PIT (periphyton index of trophic status)
- AIP (acidification index periphyton)

## TODO

- HBI2
- functions to calculate nEQR normalization


## Release process

1. do appropriate changes, either locally or on a branch
2. commit changes on main
3. bump the version number in [pyproject.toml](./pyproject.toml#L3)
4. push to main branch. This triggers deploy job in (github actions)[https://github.com/NIVANorge/begroing-index/actions]
5. new version should appear at https://pypi.org/project/begroing-index/
