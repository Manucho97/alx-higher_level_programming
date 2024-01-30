#!/usr/bin/python3

def uppercase(str):
    i = len(str)
    j = 0
    while j < i:
        c = str[i]
        unicode1 = ord(c)
        if 65 <= unicode1 <= 90:
            print("{:c}".format(c))
        else:
            unicode1 = unicode1 - 32
            c = chr(unicode1)
            print("{}".format(c))
        j = j + 1
