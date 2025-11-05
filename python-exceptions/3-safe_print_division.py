#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divde = a / b
    except (TypeError, ZeroDivisionError):
        divide = None
    finally:
        print("Result: {}".format(divide))
    return (divide)
