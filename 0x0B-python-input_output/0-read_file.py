#!/usr/bin/python3
'''module for 0-read_file.py'''


def read_file(filename=""):
    '''reads a file'''
    with open(filename, encoding='utf-8') as f:
        txt = f.read()
    print(txt, end='')
