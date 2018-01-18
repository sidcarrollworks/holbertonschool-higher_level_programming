#!/usr/bin/python3
class Student:

	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def to_json(self, attrs=None):
		new_dict = {}
		if type(attrs) is list:
			#get attributes form list
			for x in attrs:
				if type(x) is not str:
					new_dict = self.__dict__
					break
				try:
					new_dict[x] = getattr(self, x)
				except:
					pass
		else:
			new_dict = self.__dict__
		return new_dict
