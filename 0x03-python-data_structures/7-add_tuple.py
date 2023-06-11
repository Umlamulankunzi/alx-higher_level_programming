#!/usr/bin/python3
def prepare_tuple(tup):
    if len(tup) >= 2:
        return (tup[0], tup[1])
    elif len(tup) == 1:
        return (tup[0], 0)
    return (0, 0)


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = prepare_tuple(tuple_a)
    tuple_b = prepare_tuple(tuple_b)

    return tuple(map(lambda n1, n2: n1 + n2, tuple_a, tuple_b))
