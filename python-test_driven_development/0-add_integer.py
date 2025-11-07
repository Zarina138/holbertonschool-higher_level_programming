#!/usr/bin/python3
"""
This module defines a function that adds two integers.
"""
def add_integer(a, b=98):
    """Add two integers or floats."""
    try:
        a = int(a)
    except Exception:
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except Exception:
        raise TypeError("b must be an integer")

    return a + b
