#!/usr/bin/python3
'''module 9-rectangle.py'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''rctngl clss'''
    def __init__(self, width, height):
        '''Initialize object'''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        '''funky fun'''
        return self.__height * self.__width

    def __str__(self):
        '''str fun that do it's job'''
        return f"[Rectangle] {self.__width}/{self.__height}"
