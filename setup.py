#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from codecs import open
from os import path
from shutil import copy
from sys import platform

from setuptools import Extension, setup

version = '0.0.1'

setup(
    name='snowflake-connector-python-lite',
    author='Manuel Garrido',
    version=version,
    description="Snowflake Connector for python LITE!",
    license='Apache License, Version 2.0',
    use_2to3=False,
    namespace_packages=['snowflake'],
    packages=[
        'snowflake.connector',
        'snowflake.connector.tool',
    ],
    python_requires='>=3.5',
    install_requires=[
        'asn1crypto>0.24.0,<2.0.0',
        'botocore',
        'jwt',
        'oscrypto<2.0.0',
        'pycryptodomex',
        'pyOpenSSL>=16.2.0',
        'pytz',
        'requests==2.22.0',
        'urllib3>=1.20,<1.26.0'
    ],

)
