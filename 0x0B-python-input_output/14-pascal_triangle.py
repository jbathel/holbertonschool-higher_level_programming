#!/usr/bin/python3
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i)//(factorial(j) * factorial(i - j)))
        triangle.append(row)
    return triangle
