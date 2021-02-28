#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the "upload" functionality of this file, you must:
#   $ pip install twine

import io
import os
from shutil import rmtree
import sys

from setuptools import Command, find_packages, setup

# Package meta-data.
NAME = "catalyst-codestyle"
VERSION = "21.03rc1"
DESCRIPTION = "Catalyst.Codestyle"
URL = "https://github.com/catalyst-team/codestyle"
EMAIL = "scitator@gmail.com"
AUTHOR = "Sergey Kolesnikov"
REQUIRES_PYTHON = ">=3.6.0"

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


def load_requirements(filename):
    """Load package requirements."""
    with open(os.path.join(PROJECT_ROOT, filename), "r") as f:
        return f.read().splitlines()


def load_readme():
    """Load package readme."""
    readme_path = os.path.join(PROJECT_ROOT, "README.md")
    with io.open(readme_path, encoding="utf-8") as f:
        return f"\n{f.read()}"


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print(f"\033[1m{s}\033[0m")

    def initialize_options(self):
        """@TODO: Docs. Contribution is welcome"""
        pass

    def finalize_options(self):
        """@TODO: Docs. Contribution is welcome"""
        pass

    def run(self):
        """Run upload command."""
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(PROJECT_ROOT, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system(f"{sys.executable} setup.py sdist bdist_wheel --universal")  # noqa: E501, S605

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")  # noqa: S605, S607

        self.status("Pushing git tags…")
        os.system(f"git tag v{VERSION}")  # noqa: S605
        os.system("git push --tags")  # noqa: S605, S607

        sys.exit()


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
    packages=find_packages(exclude=("tests", )),
    scripts=[
        "bin/catalyst-check-codestyle",
        "bin/catalyst-make-codestyle",
        "bin/catalyst-codestyle-flake8",
        "bin/catalyst-codestyle-isort",
    ],
    install_requires=load_requirements("requirements.txt"),
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
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    # $ setup.py publish support.
    cmdclass={
        "upload": UploadCommand,
    },
)
