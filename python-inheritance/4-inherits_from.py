#!/usr/bin/python3
"""
This module provides the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited from a_class.
    """
    if isinstance(obj, a_class):
        return type(obj) != a_class
    return False
