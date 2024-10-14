# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "authentik_openapi"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="authentik",
    author_email="hello@goauthentik.io",
    url="",
    keywords=["OpenAPI", "authentik"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['authentik_openapi=authentik_openapi.__main__:main']},
    long_description="""\
    Making authentication simple.
    """
)

