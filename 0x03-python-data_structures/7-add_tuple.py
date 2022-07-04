#!/usr/bin/python3
def add_tuple(tuple_x=(), tuple_y=()):
    tuple_x += (0, 0)
    tuple_y += (0, 0)
    return (tuple_x[0] + tuple_y[0], tuple_x[1] + tuple_y[1])
