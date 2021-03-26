#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for cp4s-connector-sdk Python Module """

from setuptools import setup, find_packages

from os import path
import io

this_directory = path.abspath(path.dirname(__file__))

with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="cp4s-connector-sdk",
    version="0.0.3",
    license="MIT",
    packages=find_packages(),

    # This SDK depends on resilient_sdk which depends on resilient as well as other python modules
    install_requires=[
        "resilient_sdk"
    ],

    include_package_data=True,

    # Add command line: connector-sdk
    entry_points={
        "console_scripts": ["connector-sdk=cp4s_connector_sdk.sdk:main"]
    },

    # PyPI metadata
    author="Ryan Gordon",
    author_email="ryan.gordon1@ibm.com",
    description="Python SDK for developing Connectors for the Cloud Pak for Security Platform",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="ibm cloud pak cp4s connector udi car",
)
