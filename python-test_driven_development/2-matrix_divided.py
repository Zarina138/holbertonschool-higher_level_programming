#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix: list of lists of integers or floats
        div: number to divide all elements by

    Returns:
        A new matrix with elements divided and rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   or div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div == float('inf') or div == float('-inf'):
        return [[0.0 for _ in row] for row in matrix]

    if not matrix or not isinstance(matrix, list):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    row_len = None
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(msg)

        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg)

    new_matrix = []
    for row in matrix:
        new_row = [round(item / div, 2) for item in row]
        new_matrix.append(new_row)

    return new_matrix
