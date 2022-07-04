#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a_list = my_list[:]
    if 0 <= idx or idx < len(a_list):
        a_list[idx] = element
        return (a_list)
    return (my_list)
