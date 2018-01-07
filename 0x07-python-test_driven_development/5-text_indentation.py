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

    for x in text:
        print('{}'.format(x), end='')
        if x == '.' or x == ':' or x == '?':
            print('')
