#!/usr/bin/python3
"""
This file makes a Square class with a private size.
"""


class Square:
    """
    A Square class that has a size.
    The size is private for now.
    """

    def __init__(self, size):
        """
        Starts a new Square.

        Args:
            size: The size of the square.
        """
        self.__size = size

