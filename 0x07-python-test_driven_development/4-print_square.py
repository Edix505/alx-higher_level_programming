#!/usr/bin/python3
'''printing squares'''


def print_square(size):
    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for x in range(size):
        for a in range(size):
            print('#', end='')
        print()
