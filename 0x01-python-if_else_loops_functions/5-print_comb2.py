#!/usr/bin/python3
for x in range(0, 100):
    if x < 99:
        print("{:02}, ".format(x), end="")
    else:
        print("{:d}".format(x))
