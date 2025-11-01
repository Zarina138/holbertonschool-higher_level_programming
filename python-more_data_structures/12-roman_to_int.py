#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for ch in roman_string:
        value = roman_dict.get(ch, 0)
        if prev_value < value and prev_value != 0:
            total = total - prev_value
        
        total = total + value
        prev_value = value

    return total
