#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_lst = my_list[:]

    if idx < 0 or idx > (len(my_list) - 1):
        return new_lst

    new_lst[idx] = element
    return new_lst
