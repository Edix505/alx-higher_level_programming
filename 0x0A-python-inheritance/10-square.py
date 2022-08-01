#!/usr/bin/python3
'''module 10-square.py'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''rctngl clss'''
    def __init__(self, size):
        '''initialize sqr'''
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        '''get measurment'''
        return self.__size ** 2
