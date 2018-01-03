#!/usr/bin/python3
class Square:
	'''
		define square
	'''
    def __init__(self, size=0):
		'''Initialization of instance attributes
            Args:
            size (int): Zero or positve number.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be a integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
		'''Calculates the area
            Return: The current square area.
        '''
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
		'''Updating the private attributes
            Args:
            value (int): Zero or positve number.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be a integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
