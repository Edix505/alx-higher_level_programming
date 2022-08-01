#!/usr/bin/python3
'''task 9 module'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''sqr clss'''
    def __init__(self, size):
        '''initialize sqr'''
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        '''get area'''
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
