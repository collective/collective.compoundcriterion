"""Installer for the collective.compoundcriterion package."""

from setuptools import find_packages
from setuptools import setup

long_description = (
    open("README.rst").read()
    + "\n"
    + "Contributors\n============\n"
    + "\n"
    + open("CONTRIBUTORS.rst").read()
    + "\n"
    + open("CHANGES.rst").read()
    + "\n"
)

setup(
    name="collective.compoundcriterion",
    version="1.0.0.dev0",
    description="Compound criterion for plone.app.collection managing complex query",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Addon",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="Plone collection criterion",
    author="IMIO",
    author_email="support@imio.be",
    url="http://pypi.python.org/pypi/collective.compoundcriterion",
    license="GPL",
    packages=find_packages("src", exclude=["ez_setup"]),
    python_requires=">=3.10",
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "imio.helpers",
        "plone.api",
        "plone.base",
        "plone.z3cform",
        "Products.CMFPlone",
        "Products.GenericSetup",
        "zope.component",
        "zope.globalrequest",
        "zope.i18nmessageid",
        "zope.interface",
        "zope.publisher",
        "zope.schema",
    ],
    extras_require={
        "test": [
            "ftw.labels",
            "plone.app.querystring",
            "plone.app.robotframework",
            "plone.app.testing",
            "plone.app.textfield",
            "plone.browserlayer",
            "plone.registry",
            "plone.testing",
            "robotsuite",
            "transaction",
            "zope.i18n",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
