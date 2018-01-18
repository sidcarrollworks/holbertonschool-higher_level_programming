#!/usr/bin/python3
def number_of_lines(filename=""):
    line_c = 0
    with open(filename, 'r') as f:
        for line in f:
            line_c += 1
    return line_c
