#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if len(my_list):
        for num in my_list:
            print("{}".format(num))
    else:
        print()