#!/usr/bin/python3
for ascii_val in range(97, 123):
    if ascii_val not in (101, 113):
        print("{}".format(chr(ascii_val)), end="")
