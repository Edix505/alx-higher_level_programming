#!/usr/bin/python3
'''module for 100-append_after.py'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts a line of text to a file'''
    with open(filename, mode='r', encoding='utf-8') as f:
        lin = f.readlines()

    with open(filename, mode='w', encoding='utf-8') as f:
        NL = []
        for x in range(len(lin)):
            NL.append(lin[x])
            if search_string in lin[i]:
                NL.append(new_string)
        f.writelines(NL)
