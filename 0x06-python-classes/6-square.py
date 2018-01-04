#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for col in range(self.__size):
            print(' ' * self.__position[0], end='')
            for row in range(self.__size):
                print('#', end='')
            print('')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__size

    @position.setter
    def position(self, value):
        error = 'position must be a tuple of 2 positive integers'
        if type(value) is not tuple and len(value) is not 2:
            if value[:2] < 0:
                raise TypeError(error)
        self.__position = value
