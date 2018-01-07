#!/usr/bin/python3
"""
    Add newlines to text block
"""


def text_indentation(text):
    """this function adds indentation

    Args:
        test (str): text block
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    tests = ['.', ':', '?']
    string = ''
    for x in text:
        string += x
        if x in tests:
            string += '\n'
            print(string.strip(' '))
            string = ''
    if x not in tests:
        print(string)
