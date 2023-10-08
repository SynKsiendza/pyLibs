import os
import sys
import time
import random
import getkey

def writeLine(filename, stringToWrite):
    f = open(filename, "a")
    f.write(stringToWrite)
    f.close()


def writeLineReplace(filename, stringToWrite):
    f = open(filename, "w")
    f.write(stringToWrite)
    f.close()

## size = bytes to read

def readFile(filename, size):
    f = open("demofile.txt", "r")
    return f.read(size)

def fileRename(filename, renameTo):
    os.rename(filename, renameTo)

def fileRemove(filename):
    os.remove(filename)