#!/usr/bin/python3
from models.base import Base
'''
    Rectangle class
'''

class Rectangle(Base):


    """Magic Funtions"""
    def __init__(self, width, height, x=0, y=0, id=None):
        inputcheck(width, height, x, y)
        wandhvalue(width, height)
        xandy(x, y)
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x,\
                                     self.y, self.width, self.height)

    """Setters and getters"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    """other methods"""
    def area(self):
        return self.__width * self.__height

    def display(self):
        rect = ""
        for x in range(self.__y):
            rect += '\n'
        for x in range(self.__height):
            rect += ' ' * self.__x
            for y in range(self.__width):
                rect += "#"
            rect += '\n'
        print(rect[:-1])

    def update(self, *args):
        numarg = len(args)
        if numarg != 0:
            for x, arg in enumerate(args):
                if x == 0:
                    self.id = arg
                if x == 1:
                    self.width = arg
                if x == 2:
                    self.height = arg
                if x == 3:
                    self.x = arg
                if x == 4:
                    self.y = arg

def inputcheck(width, height, x, y):
    if not type(width) == int:
        raise TypeError('width must be an integer')
    if not type(height) == int:
        raise TypeError('height must be an integer')
    if not type(x) == int:
        raise TypeError('x must be an integer')
    if not type(y) == int:
        raise TypeError('y must be an integer')

def wandhvalue(width, height):
    if width <= 0:
        raise ValueError('width must be > 0')
    if height <= 0:
        raise ValueError('height must be > 0')

def xandy(x, y):
    if x < 0:
        raise ValueError('x must be >= 0')
    if y < 0:
        raise ValueError('y must be >= 0')
