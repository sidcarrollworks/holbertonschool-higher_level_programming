#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for x in sorted(my_dict.keys()):
        print('%s: %s' % (x, my_dict[x]))
