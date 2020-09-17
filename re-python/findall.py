#!/usr/bin/python3
import re

filename = "/etc/passwd"
f = open(filename)
text = f.read()
f.close()
regex = "bash"
x = re.findall(regex , text)
for i in x:
    print(i.strip())
