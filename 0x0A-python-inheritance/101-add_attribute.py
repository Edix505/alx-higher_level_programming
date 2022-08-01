#!/usr/bin/python3
'''module 101-add_attribute.py'''


def add_attribute(object, name, value):
    '''sums new attrib to the obj if possible'''
    if '__dict__' in dir(object):
        object.__dict__[name] = value
    else:
        raise TypeError("can't sum new attrib")
