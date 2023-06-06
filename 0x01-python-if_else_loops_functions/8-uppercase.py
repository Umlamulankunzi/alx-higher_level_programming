#!/usr/bin/python3
def uppercase(str):
    for ltr in str:
        if ord(ltr) in range(97, 123):
            ltr = chr(ord(ltr) - 32)
        print(f"{ltr}", end="")
    print()
