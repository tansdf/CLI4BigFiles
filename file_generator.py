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
@click.option('--size', help='File size.')
@click.option('--modify', is_flag=True)
@click.option('--increase', is_flag=True)
@click.option('--percent', help='File size.')

def hello(file_name, size, modify, increase, percent):
    if size.endswith('G'):
        writesize = int(size[:-1])*1024*1024*1024
    elif size.endswith('M'):
        writesize = int(size[:-1])*1024*1024
    elif size.endswith('K'):
        writesize = int(size[:-1])*1024
    else:
        writesize = int(size)
    with open(file_name, 'w') as f:        
            f.write(''.join(random.choice(string.ascii_letters) for i in range(writesize)))

if __name__ == '__main__':
    hello()

