#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    for x in argv[1:]:
        sum += int(x)
    print("{}".format(sum))
