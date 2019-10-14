#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Function to divide a matrix by a given number"""
    if not isinstance(matrix, list):
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
    if not isinstance(div, (int, float)):
        raise TypeError(
                'div must be a number')
    if div == 0:
        raise ZeroDivisionError(
                'division by zero')
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError(
                    'Each row of the matrix must have the same size')
    else:
        return [[round(i / div, 2) for i in row] for row in matrix]
