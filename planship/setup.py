from pathlib import Path

from setuptools import find_packages, setup  # noqa: H301

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

NAME = "planship"
VERSION = "0.2.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "planship_openapi_gen >= 1",
]

project_urls = {
    "Repository": "https://github.com/planship/planship-python",
    "Planship Docs": "https://docs.planship.io",
    "Class Reference": "https://github.com/planship/planship-python/blob/master/docs/content/planship-class.md",
}

setup(
    name=NAME,
    version=VERSION,
    description="Planship API client",
    author="Pawel Wojnarowicz",
    author_email="pawel@planship.io",
    url="https://planship.io",
    keywords=["Planship"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls=project_urls,
)
