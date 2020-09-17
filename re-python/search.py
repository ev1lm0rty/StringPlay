#!/usr/bin/python3

import re

filename = "/etc/passwd"
f = open(filename)
text = f.read()
f.close()
regex = "morty"
x = re.search(regex , text)
print(x)
print(x.group())
