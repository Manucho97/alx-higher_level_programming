#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    for row in matrix:
        for i in row:
            print(i, end='')
        print()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

square_matrix_simple(matrix)
