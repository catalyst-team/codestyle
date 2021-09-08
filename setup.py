#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Iterable, Union
from pathlib import Path

from setuptools import find_packages, setup

# Package meta-data.
NAME = "catalyst-codestyle"
VERSION = "21.09"
DESCRIPTION = "Catalyst.Codestyle"
URL = "https://github.com/catalyst-team/codestyle"
EMAIL = "scitator@gmail.com"
AUTHOR = "Sergey Kolesnikov"
REQUIRES_PYTHON = ">=3.6.0"

PROJECT_ROOT = Path(__file__).parent.resolve()


def load_requirements(filename: Union[Path, str] = "requirements.txt") -> Iterable[str]:
    """Load package requirements."""
    with open(PROJECT_ROOT / filename) as f:
        return f.read().splitlines()


def load_readme(filename: Union[Path, str] = "README.md") -> str:
    """Load package readme."""
    with open(PROJECT_ROOT / filename, encoding="utf-8") as f:
        return f"\n{f.read()}"


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=load_readme(),
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    download_url=URL,
    project_urls={
        "Bug Tracker": "https://github.com/catalyst-team/codestyle/issues",
        "Documentation": "https://catalyst-team.github.io/catalyst",
        "Source Code": "https://github.com/catalyst-team/codestyle",
    },
    packages=find_packages(exclude=("tests",)),
    entry_points={
        "console_scripts": [
            "catalyst-codestyle-flake8=codestyle._flake8:main",
            "catalyst-codestyle-isort=codestyle._isort:main",
        ],
    },
    scripts=["bin/catalyst-check-codestyle", "bin/catalyst-make-codestyle"],
    install_requires=load_requirements(),
    include_package_data=True,
    license="Apache License 2.0",
    classifiers=[
        "Environment :: Console",
        "Natural Language :: English",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        # Audience
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        # Programming
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
