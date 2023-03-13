#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    t11 = tuple_a[0] if len(tuple_a) > 0 else 0
    t12 = tuple_a[1] if len(tuple_a) > 1 else 0
    t21 = tuple_b[0] if len(tuple_b) > 0 else 0
    t22 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (t11 + t21, t12 + t22,)
