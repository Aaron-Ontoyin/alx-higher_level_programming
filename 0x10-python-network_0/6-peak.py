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
    if list_of_integers is None:
        return None

    list_len = len(list_of_integers)
    if list_len == 0:
        return None

    if list_len == 1:
        return list_of_integers[0]

    mid_idx = list_len // 2

    if mid_idx != list_len - 1:
        mid_val = list_of_integers[mid_idx]
        left_val = list_of_integers[mid_idx - 1]
        right_val = list_of_integers[mid_idx + 1] 

        if left_val < mid_val and right_val < list_of_integers[mid_idx]:
            return list_of_integers[mid_idx]
    else:
        mid_val = list_of_integers[mid_idx]
        left_val = list_of_integers[mid_idx - 1]

        return (mid_val if left_val < mid_val else left_val)

    if left_val > mid_val:
        sublist = list_of_integers[0:mid_idx]
    else:
        sublist = list_of_integers[mid_idx + 1:]

    return find_peak(sublist)
