#!/usr/bin/python3

import re

def openFile(filename):
    f = open(filename , "r")
    return f

# Findall
## Returns a list containing all matches
def findAll(string):
    x = re.findall("bash" , string)
    y = re.findall("morty" , repr(string))
    print(y)

def main():
    f = openFile("/etc/passwd")
    lines = f.read()
    searchString(lines)
    f.close()


# Search
## Matching a string
### Return None if the pattern doesnt match
### Returns Match object if it finds

def searchString(string):
    string = repr(string) # Converts to raw string
    # matchObject = re.search(pattern, input_str, flags=0)
    regex = r"*morty*"
    #x = re.search(regex , string)
    x = re.search(regex , "morty:x:1000:1000:Morty,,,:/home/morty:/bin/bash")
    print(x)

main()
