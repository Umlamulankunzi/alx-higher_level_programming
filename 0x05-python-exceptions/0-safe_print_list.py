#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_printed = 0

    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            num_printed += 1

        except IndexError:
            pass

    print()
    return num_printed
