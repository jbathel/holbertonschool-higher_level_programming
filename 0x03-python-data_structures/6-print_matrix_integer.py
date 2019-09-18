#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                print('{}'.format(matrix[row][col]), end='')
                if col + 1 < len(matrix[0]):
                    print(' ', end='')
            print()
