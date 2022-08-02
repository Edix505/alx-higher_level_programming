#!/usr/bin/python3
'''module for 6-load_from_json_file.py'''


import json


def load_from_json_file(filename):
    '''loads json and convert to pyobject'''
    with open(filename, mode='r', encoding='utf-8') as f:
        my_object = json.load(f)
    return my_object
