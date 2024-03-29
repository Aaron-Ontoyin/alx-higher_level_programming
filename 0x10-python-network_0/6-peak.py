#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers (list): List of integers to find peak in.
    Returns:
        Peak of the list_of_integers(int) or None if the list is empty.
    """
    list_len = len(list_of_integers)

    if list_len == 0:
        return None

    left = 0
    right = list_len - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
