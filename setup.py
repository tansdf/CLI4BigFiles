# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 02:30:35 2019

@author: tansdf
"""

from setuptools import setup, find_packages

setup(
    name='mypkg',
    version='0.1',
    packages=find_packages(),
    install_requires=['click'],
    entry_points={
        'console_scripts': ['cli=cli.cli:cli'],
    },
)