#!/usr/bin/python3
"""Defines the Square class."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Create a square and set its size.

        Args:
            size (int): The size of the square (default = 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the square's area."""
        return self.__size ** 2
