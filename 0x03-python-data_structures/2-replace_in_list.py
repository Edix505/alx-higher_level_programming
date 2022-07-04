#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
   """Replace element of list"""
    if 0 <= idx or idx < len(my_list):
        my_list[idx] = element
    return (my_list)
