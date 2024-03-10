#!/usr/bin/python3

def max_integer(my_list=[]):
    n = 0
    for number in my_list:
        if len(my_list) == 0:
            n = None
        else:
            if number > n:
                n = number
    return n
