#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    n = len(my_list)
    if idx > n or idx < 0:
        return new_list
    else:
        for i, item in enumerate(new_list):
            if i == idx:
                new_list[i] = element
        return new_list
