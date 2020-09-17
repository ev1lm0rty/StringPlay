#!/usr/bin/python3
import re

filename = "/etc/passwd"
f = open(filename)
text = f.read()
regex = "bash"
f.close()
x = re.match(regex , text)
print(x)
