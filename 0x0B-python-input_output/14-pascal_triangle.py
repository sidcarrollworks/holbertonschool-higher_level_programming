#!/usr/bin/python3

def pascal_triangle(n):
	new_list = []
	if n <= 0:
		return new_list
    arr = [[1]]
    for i in range(n - 1):
        arr.append(
            [x + n for x, n in zip(arr[-1] + [0], [0] + arr[-1])]
        )
    return arr
