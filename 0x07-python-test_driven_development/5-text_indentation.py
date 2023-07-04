#!/usr/bin/python3

"""
Module
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line_chars = ".?:"
    del_space_flag = False

    for ltr in text:
        if del_space_flag:
            if ltr == " ":
                continue
            else:
                del_space_flag = False

        if ltr in new_line_chars:
            print("\n\n", end="")
            del_space_flag = True
            continue
        print(ltr, end="")
