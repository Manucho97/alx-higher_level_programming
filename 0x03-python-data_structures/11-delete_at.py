#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        for i, number in enumerate(my_list):
            if i != idx:
                new_list.append(number)
        return new_list
