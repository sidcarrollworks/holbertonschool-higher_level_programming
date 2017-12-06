#!/usr/bin/python3
for x in range(0, 10):
    for i in range(0, 10):
        if (x < i):
            print('{}{}'.format(x, i), end='')
            if (x < 8):
                print(', ', end='')
print('\n', end='')
