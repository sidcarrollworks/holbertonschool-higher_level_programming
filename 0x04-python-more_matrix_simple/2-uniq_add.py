#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    my_list = list(set(my_list))
    for x in my_list:
        add += x
    return add
