#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for sub_list in matrix:
        n_matrix.append(list(map(lambda x: x*x, sub_list)))

    return n_matrix
