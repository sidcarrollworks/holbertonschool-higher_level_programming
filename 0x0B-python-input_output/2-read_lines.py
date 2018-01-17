#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
	with open(filename, 'r') as f:
		if nb_lines <= 0:
			lines = f.read()
			print(lines, end ="")
		else:
			lines = [lines for lines in f][:nb_lines]
			print(lines)
