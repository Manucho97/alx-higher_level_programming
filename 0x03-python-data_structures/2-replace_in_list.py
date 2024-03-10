#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    n = len(my_list)
    if idx > n or idx < 0:
        return my_list
    else:
        for i, item in enumerate(my_list):
            if i == idx:
                my_list[i] = element
        return my_list
