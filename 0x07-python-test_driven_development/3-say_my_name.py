#!/usr/bin/python3
"""
    Prints my name is <input name>
"""

def say_my_name(first_name, last_name=""):
    """Prints a name

    Args:
        first_name (string): first name string
        last_name (string): last name string
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {:s} {:s}'.format(first_name, last_name))
