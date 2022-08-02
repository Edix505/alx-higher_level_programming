#!/usr/bin/python3
'''module for 12-pascal_triangle.py'''


def pascal_triangle(n):
    '''the Pascal’s triangle of n
    '''
    if n <= 0:
        return list()

    x = []
    for line in range(0, n):
        # Every line has number of
        # integers equal to line
        # number
        tmp = []
        for a in range(0, line + 1):
            tmp.append(magic(line, a))
        x.append(tmp)
    return x


def magic(n, k):
    '''magic function that does some magic'''
    res = 1
    if (k > n - k):
        k = n - k
    for a in range(0, k):
        res = res * (n - a)
        res = res // (a + 1)
    return res
