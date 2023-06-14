#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = []
    for elem in my_list:
        if elem == search:
            n_list.append(replace)
        else:
            n_list.append(elem)

    return n_list
