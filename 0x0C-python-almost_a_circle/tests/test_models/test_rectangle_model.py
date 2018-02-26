#!/usr/bin/python3
"""Tests for the rectangle"""
import unittest
import os
from models.rectangle import Rectangle


class test_RectangleClass(unittest.TestCase):
    """
        triangle class test
    """

    def test_width_and_height(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5); self.assertEqual(r.height, 10)
        r.width = 10; r.height = 5
        self.assertEqual(r.width, 10); self.assertEqual(r.height, 5)
        del r

    def test_x_and_y(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5); self.assertEqual(r.height, 10)
        r.width = 10; r.height = 5
        self.assertEqual(r.width, 10); self.assertEqual(r.height, 5)
        del r

    def test_rect_id(self):
        r = Rectangle(5, 10, 5, 5, 1337); r1 = Rectangle(10, 15)
        self.assertEqual(r.id, 1337); self.assertEqual(type(r1.id), int)
        del r

    def test_w_passing_negVal(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10)

    def test_h_passing_negVal(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, -10)

    def test_w_passing_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle("10", "5")

    def test_w_passing_list(self):
        with self.assertRaises(TypeError):
            r = Rectangle([10], 5)

    def test_h_passing_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, "10")

    def test_h_passing_list(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, [10])

    def test_w_passing_zero(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 13)

    def test_h_passing_zero(self):
        with self.assertRaises(ValueError):
            r = Rectangle(3, 0)

    def test_w_passing_float(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1.337, 5)

    def test_h_passing_float(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 1.337)


    def test_passing_nothing(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_x_passing_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 5, "8", 4)

    def test_x_passing_list(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 5, [6], 4)

    def test_y_passing_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 2, 10, "3")

    def test_y_passing_list(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, 4, [5])

    def test_x_with_negval(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -8, 8)

    def test_y_with_negval(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 8, -8)

    def test_xy_passing_nothing(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.x + r.y, 0)
        del r

    def test_area(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 10 * 5)
        del r

    def test__str__(self):
        r = Rectangle(5, 10, 30, 33, 55)
        self.assertEqual(str(r), "[Rectangle] (55) 30/33 - 5/10")
        del r

    def test_update_all_args(self):
        r = Rectangle(10, 15, 50, 50, 55)
        r.update(100, 30, 40, 10, 10)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        del r

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 15, 50, 50, 55)
        r.update(100, 30, id=69)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 50)
        self.assertEqual(r.y, 50)
        del r

    def test_update_args_with_kwargs(self):
        r = Rectangle(10, 15, 50, 50, 55)
        r.update(100, 30, height=69, x=2)
        self.assertEqual(r.id, 100)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 69)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 50)
        del r

    def test_update_all_kwargs(self):
        r = Rectangle(10, 15, 50, 50, 55)
        r.update(width=100, id=30, height=69, y=2, x=4)
        self.assertEqual(r.id, 30)
        self.assertEqual(r.width, 100)
        self.assertEqual(r.height, 69)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)
        del r

    def test_toDict_type(self):
        r = Rectangle(5, 10)
        self.assertEqual(type(r.to_dictionary()), dict)
        del r

    def test_toDict_dict(self):
        r = Rectangle(10, 15, 5, 5, 55)
        self.assertEqual(r.to_dictionary(), {'width': 10, 'height': 15,'x': 5, 'y': 5, 'id': 55})

    def test_saving_file(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        r = Rectangle(10, 15, 5, 5, 1337)
        r.save_to_file([r])
        tmp = '[{"width": 10, "height": 15, "x": 5, "y": 5, "id": 1337}]'
        with open("Rectangle.json", "r") as f:
            tmpFile = f.read()
        self.assertEqual(type(tmp), type(tmpFile))
        del r

    def test_saving_file_with_none(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        tmp = '[]'
        with open("Rectangle.json", "r") as f:
            tmpFile = f.read()
        self.assertEqual(tmp, tmpFile)

    def test_dict_toStr_toDict(self):
        listDict = [{'width': 10, 'height': 5, 'x': 10, 'y': 10, 'id': 555}]
        testDict = {'width': 10, 'height': 5, 'x': 10, 'y': 10, 'id': 555}
        jsonStr = Rectangle.to_json_string(listDict)
        back2Dict = Rectangle.from_json_string(jsonStr)
        self.assertEqual(back2Dict[0], testDict)


    def test_create(self):
        r = Rectangle(5, 10, 5, 5, 555)
        tmpDict = r.to_dictionary()
        newRect = Rectangle.create(**tmpDict)
        self.assertIsNot(r, newRect)
        self.assertEqual(type(newRect), Rectangle)
        self.assertEqual(newRect.to_dictionary(), {
            'id': 555,
            'width': 5,
            'height': 10,
            'x': 5,
            'y': 5
        })

    def test_load_fromFile_nonExist(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        tmp = Rectangle.load_from_file()
        self.assertEqual(tmp, [])

    def test_load_fromFile(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

        r = Rectangle(10, 15, 5, 5, 1337)
        r.save_to_file([r])
        tmp = r.load_from_file()

        self.assertEqual(type(tmp[0]), Rectangle)
        self.assertEqual(tmp[0].to_dictionary(), {
            'id': 1337,
            'width': 10,
            'height': 15,
            'x': 5,
            'y': 5
        })
