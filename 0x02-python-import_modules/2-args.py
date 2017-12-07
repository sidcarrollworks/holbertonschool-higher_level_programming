#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) > 1:
        a = ":"
    else:
        a = "."
    print("{} arguements{}".format(len(argv) - 1, a))
    i = 1
    for j in argv[1:]:
        print("{}: {}".format(i, j))
        i += 1
