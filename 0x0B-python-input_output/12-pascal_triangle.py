#!/usr/bin/python3
'''module for 12-pascal_triangle.py'''


def pascal_triangle(n):
    '''the Pascal’s triangle of y
    '''
    if y <= 0:
        return list()

    x = []
    for line in range(0, y):
        # Every line has number of
        # integers equal to line
        # number
        tmp = []
        for a in range(0, line + 1):
            tmp.append(magic(line, a))
        x.append(tmp)
    return x


def magic(y, k):
    '''magic function that does some magic'''
    res = 1
    if (k > y - k):
        k = y - k
    for a in range(0, k):
        res = res * (y - a)
        res = res // (a + 1)
    return res
