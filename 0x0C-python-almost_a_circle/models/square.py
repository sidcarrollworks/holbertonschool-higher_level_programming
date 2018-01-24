#!/usr/bin/python3
'''square module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        Square class
    '''

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y, self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
            updates rectangle
        '''
        words = ["id", "size", "x", "y"]
        if kwargs is not None:
            i = 0
            for key, value in kwargs.items():
                setattr(self, key, value)
        for x, arg in enumerate(args):
            setattr(self, words[x], arg)

    def to_dictionary(self):
        '''
            turns to dict
        '''
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
