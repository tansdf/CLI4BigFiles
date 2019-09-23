# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 01:37:56 2019

@author: tansdf
"""
            
import random
import string
import click

@click.command()
@click.option('--file-name', default="defout.tst", help='Name of file for generation.')
@click.option('--size', default=1, help='File size.')

def hello(file_name, size):
    with open(file_name, 'w') as f:
        for i in range(size):
            f.write(random.choice(string.ascii_letters))

if __name__ == '__main__':
    hello()

