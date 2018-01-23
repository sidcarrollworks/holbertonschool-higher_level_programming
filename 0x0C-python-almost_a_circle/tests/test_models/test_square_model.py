#!/usr/bin/python3
import unittest
import json
import sys
from models.square import Square


class TestSquare(unittest.TestCase):
    '''
        Tests for update
    '''

    def test_print(self):
        square = Square(5,id=77)
        self.assertEqual(str(square), '[Square] (77) 0/0 - 5')

    # def test_display(self):
        # square = Square(5)
        # self.assertEqual(square.display(), '#####\n#####\n#####\n#####\n#####\n')

    def test_area(self):
        square = Square(5)
        self.assertEqual(str(square.area()), '25')

    def test_width(self):
        square = Square(5)
        self.assertEqual(5, square.width)
