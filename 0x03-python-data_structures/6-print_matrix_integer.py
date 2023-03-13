#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            for cnt, j in enumerate(i):
                if cnt + 1 != len(i):
                    print("{:d}".format(j), end=' ')
                else:
                    print("{:d}".format(j), end='\n')
