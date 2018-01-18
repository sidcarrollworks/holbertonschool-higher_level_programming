#!/usr/bin/python3
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
from sys import argv

filename = 'add_item.json'

try:
	file_data = load_from_json_file(filename)
except FileNotFoundError:
	file_data = []
	save_to_json_file(file_data, filename)

for x in range(1, len(argv)):
	file_data.append(argv[x])

save_to_json_file(file_data, filename)
