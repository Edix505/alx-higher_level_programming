#!/usr/bin/python3
'''module 8-rectangle.py'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''rctngl clss'''
    def __init__(self, width, height):
        '''Initialize of the object'''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
