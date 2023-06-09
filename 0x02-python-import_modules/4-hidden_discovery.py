#!/usr/bin/python3
from hidden_4 import *


if __name__ == "__main__":
    var_arr = dir()
    for index in range(0, len(var_arr)):
        if var_arr[index][0:2] != "__":
            print("{}".format(var_arr[index]))
