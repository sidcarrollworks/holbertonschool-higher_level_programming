#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is '':
        char = None
    else:
        char = sentence[0]
    return (len(sentence), char)
