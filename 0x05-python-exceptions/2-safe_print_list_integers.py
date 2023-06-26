#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0

    for index in range(x):
        try:
            print("{:d}".format(int(my_list[index])), end="")
            num_printed += 1

        except ValueError:
            pass

    print()
    return num_printed
