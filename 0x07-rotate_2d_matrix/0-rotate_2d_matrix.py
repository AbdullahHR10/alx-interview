#!/usr/bin/python3
""" Module that contains solution for Rotate 2D Matrix. """


def rotate_2d_matrix(matrix):
    """ Rotates an m by n 2D matrix in place. """
    if not matrix or not all(isinstance(row, list) for row in matrix):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return
    for layer in range(rows // 2):
        first = layer
        last = rows - layer - 1
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
