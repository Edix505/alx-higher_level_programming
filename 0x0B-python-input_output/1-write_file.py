#!/usr/bin/python3
'''module for 1-write_file.py'''


def write_file(filename="", text=""):
    '''writes a string '''
    with open(filename, mode='w', encoding='utf-8') as f:
        fol = f.write(text)

    return fol
