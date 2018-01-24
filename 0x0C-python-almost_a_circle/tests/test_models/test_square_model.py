#!/usr/bin/python3
import unittest
import json
import sys
import io
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    '''
        Tests for update
    '''

    def test_print(self):
        square = Square(5,id=77)
        self.assertEqual(str(square), '[Square] (77) 0/0 - 5')

    def test_area(self):
        square = Square(5)
        self.assertEqual(str(square.area()), '25')

    def test_width(self):
        square = Square(5)
        self.assertEqual(5, square.width)

    def test_size(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        with self.assertRaises(ValueError):
            s1 = Square(0)

        with self.assertRaises(TypeError):
            s1 = Square()

    def test_x(self):
        s1 = Square(5, 2)
        s2 = Square(3, 4, 2, 4)
        s3 = Square(3, 0, 0)

        self.assertEqual(s1.x, 2)
        self.assertEqual(s2.x, 4)
        self.assertEqual(s3.x, 0)

    def test_y(self):
        s1 = Square(5, 2, 3)
        s2 = Square(3, 4, 2, 4)
        s3 = Square(3, 0, 0)

        self.assertEqual(s1.y, 3)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s3.y, 0)

    def test_id(self):
        Base._Base__nb_objects = 0
        s1 = Square(1, 3)
        s2 = Square(1, 4)
        s3 = Square(3, 0, 0, 24)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 24)

    def test_full_input(self):
        Base._Base__nb_objects = 0
        s1 = Square(4, 2, 3, 44)

        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 44)

    def test_full_input_0s(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            s1 = Square(0, 0, 0, 0)

    def test_input_type(self):
        with self.assertRaises(TypeError):
            s1 = Square("wow")

        with self.assertRaises(TypeError):
            s1 = Square([1, 2, 3])

        with self.assertRaises(TypeError):
            s1 = Square({'id': 45, 'size': 30})

        with self.assertRaises(TypeError):
            s1 = Square((1, ))

    def test_if_display(self):
        output = io.StringIO()
        sys.stdout = output

        s1 = Square(4, 3, 2, 1)

        s1_print = "\n\n   ####\n   ####\n   ####\n   ####\n"

        s1.display()

        self.assertEqual(output.getvalue(), s1_print)

        sys.stdout = sys.__stdout__

    def test_update(self):
        s1 = Square(2, 2, 2, 2)

        s1.update(3, 3, 3, 3)

        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 3)
