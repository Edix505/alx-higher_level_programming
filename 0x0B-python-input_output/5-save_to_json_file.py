#!/usr/bin/python3
'''module for 5-save_to_json_file.py'''


import json


def save_to_json_file(my_obj, filename):
    '''writes obj in json format'''
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
