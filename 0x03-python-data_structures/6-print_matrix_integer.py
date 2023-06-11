#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub_list in matrix:
        len_sublst = len(sub_list)
        for index in range(len_sublst):
            print("{}".format(sub_list[index]), end="")

            if index == len_sublst - 1:
                print()
            else:
                print(" ", end="")
