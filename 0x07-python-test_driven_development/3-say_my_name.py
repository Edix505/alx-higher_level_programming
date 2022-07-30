#!/usr/bin/python3
'''printing names'''


def say_my_name(first_name, last_name=""):
    if type(first_name) is not str:
        raise TypeError('first_name is not a string')
    elif type(last_name) is not str:
        raise TypeError('last_name is not a string')

    print(f'My name is {first_name} {last_name}')
