# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 01:37:56 2019

@author: tansdf
"""
            
import random
import string
import click
import os

def getsize(size):
    if size.endswith('G'):
            writesize = int(size[:-1])*1024*1024*1024
    elif size.endswith('M'):
            writesize = int(size[:-1])*1024*1024
    elif size.endswith('K'):
            writesize = int(size[:-1])*1024
    else:
            writesize = int(size)
    return writesize

@click.command()
@click.option('--file-name', default="defout.tst", help='Name of file for generation.')
@click.option('--size', help='File size.')
@click.option('--modify', is_flag=True)
@click.option('--increase', is_flag=True)
@click.option('--percent', help='Size for chainging/increasing.')

def hello(file_name, size, modify, increase, percent):
    buffer=getsize("2G")
    if modify:
        existedSize = os.path.getsize(file_name)
        #print(existedSize)
        percentedSize = int(existedSize/100 *percent)
        
    else:
        writesize = getsize(size)
        #if writesize
        while writesize > 0:
            if writesize > buffer:
                with open(file_name, 'w') as f:        
                    f.write(''.join(random.choice(string.ascii_letters) for _ in range(buffer)))
                writesize-=buffer
            else:
                with open(file_name, 'w') as f:        
                    f.write(''.join(random.choice(string.ascii_letters) for _ in range(writesize)))
        print("Job is done")    
        
if __name__ == '__main__':
    hello()

