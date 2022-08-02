#!/usr/bin/python3
'''module for 2-append_write.py'''


def append_write(filename="", text=""):
    '''appends txt to file'''
    with open(filename, mode='a', encoding='utf-8') as f:
        fol = f.write(text)
    return fol
