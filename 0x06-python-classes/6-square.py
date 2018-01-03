#!/usr/bin/python3
class Square:
    '''
        Define a square
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialization of instance attributes
            Args:
            size (int): Zero or positve number.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be a integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        '''Calculates the area
            Return: The current square area.
        '''
        return self.__size * self.__size

    def my_print(self):
        '''
            prints in stdout the square with the character # or a new line
            is size is zero.
        '''
        if self.__size == 0:
            print('')
        else:
            for space_c in range(self.__position[1]):
                print(' ')

            for col in range(self.__size):
                for space_r in range(self.__position[0]):
                    print(' ', end='')
                for row in range(self.__size):
                    print('#', end='')
                print()

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

    @property
    def position(self):
        return self.__size

    @position.setter
    def position(self, value):
        '''Updating the private attributes
            Args:
            value (int): tuple of two positve numbers.
        '''
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[:2], int):
                if value[:2] >= 0:
                    self.__position = value
                    return
        raise TypeError('position must be a tuple of 2 positive integers')
