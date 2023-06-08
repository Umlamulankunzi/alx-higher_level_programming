#!/usr/bin/python3
import sys


def print_args():
    num_args = len(sys.argv)

    if num_args == 1:
        print("0 arguments.")
        return

    text = "arguments" if num_args - 1 == 1 else "arguments"
    print(f"{num_args - 1} {text}:")

    for ser, arg in enumerate(sys.argv[1:], 1):
        print(f"{ser}: {arg}")


if __name__ == "__main__":
    print_args()
