#!/usr/bin/python3
'''module for 9-student.py'''


class Student:
    '''class'''
    def __init__(self, first_name, last_name, age):
        '''register of the student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''dictionary representation of studt'''
        return self.__dict__
