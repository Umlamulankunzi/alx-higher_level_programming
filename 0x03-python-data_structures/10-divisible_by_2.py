#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_lst = []
    for num in my_list:
        if num % 2 == 0:
            bool_lst.append(True)
        else:
            bool_lst.append(False)

    return bool_lst
