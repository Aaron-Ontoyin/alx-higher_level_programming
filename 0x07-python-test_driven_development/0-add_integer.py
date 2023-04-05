#!/usr/bin/python3
"""
add_integer module

This module has one function, add_integer().
"""
def check_num(n):
    """
    Checks if a number, n is a float or int
    Returns int form of the n or raises an error on failure to be an int or float
    """
    if type(n) in [int, float]:
        try:
            n = int(n)
        except:
            raise TypeError('a must be an integer')
        return n
    else:
        raise TypeError('a must be an integer')
    

def add_integer(a, b=98):
    """
    Return the addition of a and b.

    Args:
        a (int, float): the first value.
        b (int, float): the second value.
    """
    a = check_num(a)
    b = check_num(b)
    
    return a + b
