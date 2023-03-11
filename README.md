# fantasyfootball-crawler
This is an open source project that will help people access all the important statistics for fantasy football.
I want to create crawlers for both team and player statistics, and package them into neat dataframes.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![github issues](https://img.shields.io/github/issues/cocobird1/fantasyfootball-crawler)
[![codecov](https://codecov.io/gh/cocobird1/fantasyfootball-crawler/branch/main/graph/badge.svg)](https://codecov.io/gh/cocobird1/fantasyfootball-crawler)
[![Build Status](https://github.com/cocobird1/fantasyfootball-crawler/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/cocobird1/fantasyfootball-crawler/actions?query=workflow%3A%22Build+Status%22)
[![PyPI](https://img.shields.io/pypi/v/fantasyfootball-crawler)](https://pypi.org/project/fantasyfootball-crawler/)
# Overview
Fantasy football is a game played by many Americans, however most are uneducated when it comes to the various in-depth statistics that are needed to "level up" your team, and potentially win big. Most websites gloss over important statistics, or don't include all of the information needed (think FantasyPros), or perhaps include too much information (think pro-football-reference). I want to build a one-stop-shop for these important statistics.

This project is a pure python project using modern tooling. It uses a `Makefile` as a command registry, with the following commands:
- `make`: list available commands
- `make develop`: install and build this library and its dependencies using `pip`
- `make build`: build the library using `setuptools`
- `make lint`: perform static analysis of this library with `flake8` and `black`
- `make format`: autoformat this library using `black`
- `make annotate`: run type checking using `mypy`
- `make test`: run automated tests with `pytest`
- `make coverage`: run automated tests with `pytest` and collect coverage information
- `make dist`: package library for distribution
