#!/usr/bin/python3
""" Module that contains a solution to Pascal's triangle problem. """


def pascal_triangle(n):
    """ Function that returns a list of lists of integers
    representing the Pascal’s triangle of n. """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
