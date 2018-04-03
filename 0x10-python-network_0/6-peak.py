#!/usr/bin/python3
''' find peak '''


def find_peak(list_of_integers):
    ''' loop to find peak of list '''

    a = list_of_integers
    x = 0

    for x in range(0, len(a)):
        if a[x-1] < a[x] and a[x] > a[x+1]:
            peak = a[x]
        elif x == len(a):
            if a[x-1] < a[x] and a[x] > a[0]:
                peak = a[x]
        x += 1
    return peak
