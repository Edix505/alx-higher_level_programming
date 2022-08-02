#!/usr/bin/python3
'''module for 4-from_json_string.py'''


import json


def from_json_string(my_str):
    '''str is returned to python nobject format'''
    return (json.loads(my_str))
