#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
import json
import unittest


class Test_Base(unittest.TestCase):
    '''
        test base module
    '''

    def test_none(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def test_id(self):
        base = Base(50)
        self.assertEqual(base.id, 50)

    def test_zero_id(self):
        base = Base(0)
        self.assertEqual(base.id, 0)

    def test_negative_id(self):
        base = Base(-28)
        self.assertEqual(base.id, -28)

    def test_list_id(self):
        base = Base([4, 2, 3])
        self.assertEqual(base.id, [4, 2, 3])

    def test_tuple_id(self):
        base = Base((5, 2))
        self.assertEqual(base.id, (5, 2))

    def test_str_id(self):
        base = Base('wow')
        self.assertEqual(base.id, 'wow')

    def test_dict_id(self):
        base = Base({'id': 20})
        self.assertEqual(base.id, {'id': 20})

    def test_to_json_type(self):
        r1 = Rectangle(10, 3, 0, 0)
        dictionary = r1.to_dictionary()
        string = Base.to_json_string([dictionary])
        self.assertEqual(type(string), str)

    def test_to_json_value(self):
        r1 = Rectangle(10, 2, 3, 5, 7)
        dictionary = r1.to_dictionary()
        string = Base.to_json_string([dictionary])
        self.assertEqual(json.loads(string), [{'height': 2,
                         'width': 10, 'x': 3, 'y': 5, 'id': 7}])

    def test_to_json_none(self):
        r1 = Rectangle(10, 2, 3, 5, 7)
        dictionary = r1.to_dictionary()
        string = Base.to_json_string(None)
        self.assertEqual(string, '[]')

    def test_to_json_none(self):
        r1 = Rectangle(10, 2, 3, 5, 7)
        dictionary = r1.to_dictionary()
        string = Base.to_json_string([])
        self.assertEqual(string, '[]')
