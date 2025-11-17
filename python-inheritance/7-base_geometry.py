#!/usr/bin/python3
"""
Defines the BaseGeometry class with area() and integer validation.
"""


class BaseGeometry:
    """
    BaseGeometry class with an unimplemented area() method
    and a positive integer validator.
    """

    def area(self):
        """
        Raise an exception because area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that `value` is a positive integer.

        Args:
            name (str): parameter name.
            value (int): value to validate.

        Raises:
            TypeError: if `value` is not an integer.
            ValueError: if `value` <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
