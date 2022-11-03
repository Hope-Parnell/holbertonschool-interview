#!/usr/bin/python3
"""Module contains function to rotate a 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix in place"""
    [(matrix.pop(0), matrix.append(list(n))) for n in zip(*matrix[::-1])]
