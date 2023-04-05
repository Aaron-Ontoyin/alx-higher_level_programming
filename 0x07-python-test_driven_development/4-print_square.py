#!/usr/bin/python3
"""
print_square module.

This module contains one function, print_square().
"""


def print_square(size):
    """
    Print a square with the char #.

    Args:
        size (int): the length of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + '\n') * size, end='')
