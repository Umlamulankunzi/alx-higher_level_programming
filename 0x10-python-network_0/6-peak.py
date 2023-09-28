#!/usr/bin/python3
""" Find a peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """

    # Check if the list is empty
    if not list_of_integers:
        return None

    # Get the length of the list
    n = len(list_of_integers)

    # Check if the list has only one element
    if n == 1:
        return list_of_integers[0]

    # Check if the first or last element is a peak
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[n - 1] >= list_of_integers[n - 2]:
        return list_of_integers[n - 1]

    # Binary search to find a peak
    left = 1
    right = n - 2
    while left <= right:
        mid = (left + right) // 2
        if (list_of_integers[mid] >= list_of_integers[mid - 1] and
                list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            right = mid - 1
        else:
            left = mid + 1

    # No peak found
    return None
