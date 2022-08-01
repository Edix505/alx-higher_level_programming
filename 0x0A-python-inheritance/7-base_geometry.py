#!/usr/bin/python3
'''module 7-base_geometry.py'''


class BaseGeometry:
    '''emty class'''
    def __init__(self):
        '''emty init'''
        pass

    def area(self):
        '''useless function'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''another pointless function'''
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
