#!/usr/bin/python3
x = 0
while x < 9:
    y = x
    while y < 10:
        if x != y:
            if x == 8 and y == 9:
                print("{}{}".format(x, y))
            else:
                print("{}{}, ".format(x, y), end='')
        y += 1
    x += 1
