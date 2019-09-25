# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 02:30:35 2019

@author: tansdf
"""

from setuptools import setup, find_packages 
#Small script for adding all needed packages
setup(
    name='file_generator',
    version='0.6',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
            'click'                         
            ],
    entry_points='''
        [console_scripts]
        file_generator=file_generator:hello
    ''',
)