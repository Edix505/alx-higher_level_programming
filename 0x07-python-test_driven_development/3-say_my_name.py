#!/usr/bin/python3
'''This module for printing stuff'''


def say_my_name(first_name, last_name=""):
    '''This function print the string "My name is <first name> <last name>"
    args:
        f_name (str): first name
        l_name (str): last name
    returns:
        None
    '''

    if type(first_name) is not str:
        raise TypeError('f_name is not a string')
    elif type(l_name) is not str:
        raise TypeError('l_name is not a string')

    print(f'My name is {f_name} {l_name}')
