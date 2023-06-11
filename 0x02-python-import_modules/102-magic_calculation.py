from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    c = add(a, b)
    for i in range(4, 6):
        c = add(c, i)
    return c if a < b else sub(a, b)
