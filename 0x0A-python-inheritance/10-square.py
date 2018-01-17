#!/usr/bin/python3
class BaseGeometry:

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater that 0'.format(name))

class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__width)

class Square(Rectangle):

    def __init__(self, size):
        self.integer_validator("size", size)
        super().init(size, size)
        self.__size = size

    def area(self):
        return  self.__size ** 2
