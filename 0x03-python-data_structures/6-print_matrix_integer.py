#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub_list in matrix:
        for num in sub_list:
            print("{}".format(num), end="")
        print()
