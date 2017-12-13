#!/usr/bin/python3
def no_c(my_string):
    my_list=[]
    for x in my_string:
        if x != 'c' and x != 'C':
            my_list.append(x)
    new_string = ''.join(my_list)
    return new_string
