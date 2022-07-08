#!/usr/bin/python3
def multiply_by_2(a_dict):
   "new dict with values doubled"
    return {key: value * 2 for key, value in a_dict.items()}
