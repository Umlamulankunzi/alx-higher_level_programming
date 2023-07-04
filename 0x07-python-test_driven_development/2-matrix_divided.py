#!/usr/bin/python3

"""
Module defining a function that divides all elements of a matrix
"""


def validate_matrice(matrice):
    """validates a matrice:list

    Args:
        matrice (list): list of int/floats

    Raises:
        TypeError: if matrice not list
        TypeError: if elements of matrice not of type int/floats
    """
    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrice, list):
        raise TypeError(type_err)
    for val in matrice:
        if not isinstance(val, (int, float)):
            raise TypeError(type_err)


def validate_matrix(matrix):
    """validates matrix

    Args:
        matrix (list): list of lists

    Raises:
        TypeError: if matrix not of type list of lists
        TypeError: if elements of maatrix not of equal length
    """
    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    size_err = "Each row of the matrix must have the same size"
    matrice_size = None
    if not isinstance(matrix, list):
        raise TypeError(type_err)
    if len(matrix) < 2:
        raise TypeError(type_err)
    for matrice in matrix:
        validate_matrice(matrice)
        if matrice_size is None:
            matrice_size = len(matrice)
            continue
        if len(matrice) != matrice_size:
            raise TypeError(size_err)


def matrix_divided(matrix, div):
    """divides all elements of elements of matrix with div

    Args:
        matrix (list): list of lists of ints/floats
        div (int/float): number to divide with

    Raises:
        ZeroDivisionError: if div is 0
        TypeError: if div is not of type int/float

    Returns:
        list: list of lists
    """
    validate_matrix(matrix)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    new_matrix = []

    for matrice in matrix:
        new_matrix.append([round(x/div, 2) for x in matrice])
    return new_matrix
