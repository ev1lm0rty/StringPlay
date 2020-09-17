#!/usr/bin/python3
import re

filename = "/etc/passwd"
find = "bash"
replace = "shit"
f = open(filename)
text = f.read()
f.close()

a = re.sub(find , replace , text)
b = re.sub("[mM]orty" , "god" , text)
print(a)
print(b)

