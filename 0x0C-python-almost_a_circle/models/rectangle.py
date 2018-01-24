#!/usr/bin/python3
"""Rectangle"""
from models.base import Base


class Rectangle(Base):
    """
        Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y,
                                                       self.width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
            area
        '''
        return self.__width * self.__height

    def display(self):
        '''
            display
        '''
        rect = ""
        for x in range(self.__y):
            rect += '\n'
        for x in range(self.__height):
            rect += ' ' * self.__x
            for y in range(self.__width):
                rect += "#"
            rect += '\n'
        print(rect[:-1])

    def update(self, *args, **kwargs):
        '''
            update
        '''
        words = ["id", "width", "height", "x", "y"]
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for x, arg in enumerate(args):
            setattr(self, words[x], arg)

    def to_dictionary(self):
        '''
            to dictionary
        '''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
