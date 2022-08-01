#!/usr/bin/python3
'''module for 4-inherits_from.py'''


def inherits_from(obj, a_class):
    '''True if the object is an instance of a class that inherited'''
    return type(obj) != a_class and issubclass(type(obj), a_class)
