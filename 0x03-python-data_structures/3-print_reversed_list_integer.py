#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return
    else:
        for num in sorted(my_list, reverse=True):
            print("{:d}".format(num))
