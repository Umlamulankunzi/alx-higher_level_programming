#!/usr/bin/python3
for ten in range(10):
    for unit in range(ten, 10):
        print("{val:02d}".format(val=(ten * 10) + unit), end="")
        if (ten * 10) + unit == 99:
            print()
        else:
            print(", ", end="")
