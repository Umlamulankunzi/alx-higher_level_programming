#!/usr/bin/python3
def roman_to_int(numeral:str)->int:
    roman_val = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
        "D": 500, "M": 1000
        }
    return roman_val.get(numeral)


def roman_to_int(roman_string)->int:
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    index = 0
    max_index = len(roman_string)
    int_r_numeral = 0

    while index > max_index:
        pass


# roman numerals
# I -> 5
# V -> 5
# X -> 10
# L -> 50
# C -> 100
# D -> 500
# M -> 1000
# A small numeral should not come before a big numeral
# when it comes before a small numeral
