#!/usr/bin/python3
for asc_val in range(122, 96, -1):
    if asc_val % 2 != 0:
        asc_val -= 32
    print("{}".format(chr(asc_val)), end="")
