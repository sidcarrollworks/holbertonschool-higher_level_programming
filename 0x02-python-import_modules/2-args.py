#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 2:
        a = "argument."
    elif len(argv) == 1:
        a = "arguments:"
    elif len(argv) > 1:
        a = "arguments:"
    print("{} {}".format(len(argv) - 1, a))
    i = 1
    for j in argv[1:]:
        print("{}: {}".format(i, j))
        i += 1
