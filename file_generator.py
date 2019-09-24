# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 01:37:56 2019

@author: tansdf
"""
            
import random
import string
import click
import os
import fileinput
import time
from base64 import b64encode

def mygetsize(size):
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
@click.option('--percent', default=5, help='Size for chainging/increasing.')

def hello(file_name, size, modify, increase, percent):
    buffer=mygetsize("1G")
    start_time = time.time()
    if modify:
        existedSize = os.path.getsize(file_name)
        print(existedSize)
        percentedSize = int(existedSize/100 *percent)
        oldExistedSize = existedSize
        print("Percented ",percentedSize,"---",existedSize)
        with fileinput.FileInput(file_name, inplace=True, backup='.bak') as file:
            for line in file:
                changeSize = int(len(line)/100 *percent)
                forReplace = b64encode(os.urandom(changeSize)).decode('utf-8')
                if len(forReplace)!=changeSize:
                    delta = abs(len(forReplace)-changeSize)
                    forReplace=forReplace[:-delta]
                offset = random.randint(0,len(line)-len(forReplace))
                print(line.replace(line[offset:offset+len(forReplace)],forReplace))
#        while percentedSize>0:              
#            with fileinput.FileInput(file_name, inplace=True, backup='.bak') as file:               
#                for line in file:                    
#                    if percentedSize > 0:
#                        if len(line) > percentedSize:
#                            randomReplaceSize = random.randint(0, percentedSize)
#                        else:
#                            randomReplaceSize = random.randint(0, len(line))
#                        forReplace = b64encode(os.urandom(randomReplaceSize)).decode('utf-8')
#                        forReplace = ''.join(random.choice(string.ascii_letters) for _ in range(randomReplaceSize)) 
#                        if len(forReplace)>len(line): 
#                            delta = len(forReplace)-len(line)
#                            percentedSize-=len(line)                            
#                            print(line.replace(line,forReplace[:-delta]))
#                        else:
#                            delta = len(forReplace)-len(line)
#                            percentedSize-=len(forReplace)
#                            print(line.replace(line[:delta],forReplace))                   
        os.unlink(file_name + '.bak')
        print("File modified.")       
    else:
        writesize = mygetsize(size)       
        while writesize > 0:
            if writesize > buffer:
                with open(file_name, 'w') as f:        
                    f.write(b64encode(os.urandom(writesize)).decode('utf-8'))                
                writesize-=buffer
            else:
                with open(file_name, 'w') as f:        
                   # f.write(''.join(random.choice(string.ascii_letters) for _ in range(writesize)))   
                    f.write(b64encode(os.urandom(writesize)).decode('utf-8'))
                writesize=0
        print("--- %s seconds ---" % (time.time() - start_time))
        print("Creating is done. Truncating to match size")    
    existedSize = os.path.getsize(file_name)
    print(existedSize)
    if ((not modify) and existedSize > mygetsize(size)) or (modify and existedSize > oldExistedSize):        
        with open(file_name, 'rb+') as filehandle:
            if modify: sizeForCut = existedSize - oldExistedSize
            else: sizeForCut = existedSize - mygetsize(size)            
            filehandle.seek(-sizeForCut, os.SEEK_END)
            filehandle.truncate()
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Job is done")    
        
if __name__ == '__main__':
    hello()

