#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dict = dict()
    for k, v in a_dictionary.items():
        n_dict[k] = v * 2
    return n_dict
