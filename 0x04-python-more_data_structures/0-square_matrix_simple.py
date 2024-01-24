#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        square_matrix.append([col ** 2 for col in row])
    return square_matrix
