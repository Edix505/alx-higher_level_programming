#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    d_list = []
    if my_list:
        for x in my_list:
            d_list.append(False if x % 2 else True)
    return d_list
