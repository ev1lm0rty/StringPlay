#!/usr/bin/python3
import re

filename = "/etc/passwd"
f = open(filename)
text = f.read()
f.close()
regex = ":"
ll = re.split(regex , text)
for i in ll:
    print(i)

