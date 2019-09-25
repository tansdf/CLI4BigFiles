# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 01:37:56 2019

@author: tansdf
"""
            
import random
import click
import os
import fileinput
import time
from base64 import b64encode

def mygetsize(size): #This method gets size of file from input
    if size.endswith('G'):
            writesize = int(size[:-1])*1024*1024*1024
    elif size.endswith('M'):
            writesize = int(size[:-1])*1024*1024
    elif size.endswith('K'):
            writesize = int(size[:-1])*1024
    else:
            writesize = int(size)
    return writesize

#Here is the cli starts
@click.command()
@click.option('--file-name', default="defout.tst", help='Name of file for generation.')
@click.option('--size', help='File size. modifier G - gigabytes, M - megabytes, K - kilobytes, number without a modifier - bytes')
@click.option('--modify', is_flag=True, help='This flag uses to modify existing file on percent.')
@click.option('--increase', is_flag=True, help='This flag uses to increce existing file on percent.')
@click.option('--percent', default=5, help='Size for modifying/increasing.')

def hello(file_name, size, modify, increase, percent): #This is the main method of
    buffer=mygetsize("1G") #Buffer for writing in case of really big files
    start_time = time.time() #Timer of whole process
    if modify: #In cse of modifying of file
        existedSize = os.path.getsize(file_name) #Gets size of file
#        print(existedSize)        
        percentedSize = int(existedSize/100 *percent) #Gets size of modifying fragment for debug
        oldExistedSize = existedSize #Save the old file size
        print("Percented ",percentedSize,"---",existedSize) # Debug output
        with fileinput.FileInput(file_name, inplace=True, backup='.bak') as file: #File modifying with fileinput library
            sigma = 0 #This is calculation error
            for line in file:
                changeSize = len(line)/100 *percent #Size that will be modified
                changeSizeint = int(len(line)/100 *percent) #This size into integer
                sigma+=abs(changeSizeint-changeSize) # Founds calculation error and add it to error variable
                if sigma>=1: #if error is significant increase change size
                    changeSizeint+=1 
                    sigma-=1
                forReplace = b64encode(os.urandom(changeSizeint)).decode('utf-8') #Creates string for replacement
                if len(forReplace)!=changeSizeint: #Cutting to match size
                    delta = abs(len(forReplace)-changeSizeint)
                    forReplace=forReplace[:-delta]
                offset = random.randint(0,len(line)-len(forReplace)) #Random replace offset
                print(line.replace(line[offset:offset+len(forReplace)],forReplace)) #Replacing   
        os.unlink(file_name + '.bak') #Deleting of backup file
        print("File modified.")  
        
    elif increase: #In casse of increasing
        existedSize = os.path.getsize(file_name) #Gets size of file      
        writesize = int(existedSize/100 *percent) #Gets size of increasing
        neededSize = existedSize + writesize #Calculates size of file after increasing            
        while writesize > 0: #Loop for adding
            if writesize > buffer: #Checking for buffer to use
                with open(file_name, 'a') as f: #Add using buffer       
                    f.write(b64encode(os.urandom(buffer)).decode('utf-8'))                
                writesize-=buffer
            else:
                with open(file_name, 'a') as f: #Add whole size or what is left                             
                    f.write(b64encode(os.urandom(writesize)).decode('utf-8'))
                writesize=0
        print("--- %s seconds ---" % (time.time() - start_time)) #Time output
        print("Increasing is done. Truncating to match size")
        print(os.path.getsize(file_name))
        
    else: #In case of creating new file
        writesize = mygetsize(size) #Gets file size from input
        with open(file_name, 'w') as f:
            print("File created")
        while writesize > 0: #Loop for write
            if writesize > buffer: #Checking for buffer to use
                with open(file_name, 'a') as f: #Write using buffer   
                    f.write(b64encode(os.urandom(buffer)).decode('utf-8'))                
                writesize-=buffer
            else:
                with open(file_name, 'a') as f: #Write whole size or what is left         
                    f.write(b64encode(os.urandom(writesize)).decode('utf-8'))
                writesize=0
        print("--- %s seconds ---" % (time.time() - start_time)) #Time output
        print("Creating is done. Truncating to match size")
        
    existedSize = os.path.getsize(file_name) #Gets size of existing file
    print(existedSize)
    # Part for truncating 
    if (increase and existedSize > neededSize) or ((not modify) and existedSize > mygetsize(size)) or (modify and existedSize > oldExistedSize):       
        with open(file_name, 'rb+') as filehandle:
            if modify: sizeForCut = existedSize - oldExistedSize # gets size which is will be removed
            elif increase: sizeForCut = existedSize - neededSize # gets size which is will be removed
            else: sizeForCut = existedSize - mygetsize(size)    # gets size which is will be removed         
            filehandle.seek(-sizeForCut, os.SEEK_END) #Find excess
            filehandle.truncate() #Cut it away
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Job is done")    
        
if __name__ == '__main__':
    hello()

