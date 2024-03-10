#!/usr/bin/python3

def multiple_returns(sentence):
    n = len(sentence)
    new_tuple = ()
    if len(sentence) == 0:
        new_tuple = (n, '')
    else:
        c = sentence[0]
        new_tuple = (n, c)
    return new_tuple
