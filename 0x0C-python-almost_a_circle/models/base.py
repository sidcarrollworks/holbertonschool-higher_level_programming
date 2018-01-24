#!/usr/bin/python3
'''base'''
import json


class Base:
    '''
        Base class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        dumbo = cls(2,4)
        dumbo.update(**dictionary)
        return dumbo

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as f:
                fcontents = json.loads(f)
        except:
            fcontents = []
        if list_objs is not None:
            for x in list_objs:
                x = x.to_dictionary()
                dict_ready = json.loads(cls.to_json_string(x))
                fcontents.append(dict_ready)

        with open(filename, 'w') as f:
            json.dump(fcontents, f)

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'
        try:
            with open(filename, encoding='UTF8') as f:
                fcontents = json.load(f)
        except:
            return []
        instances = []

        for instance in fcontents:
            linst = cls.create(**instance)
            instances.append(linst)

        return instances

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
