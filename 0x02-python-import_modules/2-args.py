#!/usr/bin/python3
from sys import argv
print("{} arguements{}".format(len(argv) - 1, ":" if len(argv) > 1 else "."))
i = 0
for j in argv[1:]:
    print("{}: {}".format(i, j))
    i += 1
