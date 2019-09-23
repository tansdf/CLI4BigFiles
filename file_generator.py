# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 01:37:56 2019

@author: tansdf
"""
def hello(filename, size):
    with open(filename, 'w') as f:
        for i in range(size):
            f.write(random.choice(string.letters))
            
import random
import string
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file-name', const=filename, type=str, help='Name of random file')

parser.add_argument('--size', const=size, type=int,                
                    help='Size')

args = parser.parse_args()
print(args.accumulate(args.integers))
hello(filename,size)



