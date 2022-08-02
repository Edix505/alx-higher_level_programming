#!/usr/bin/python3
'''module for 11-student.py'''


class Student:
    '''student class'''
    def __init__(self, first_name, last_name, age):
        '''register the student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''return a dictionary representation of a Student instance'''
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        MD = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                MD[key] = value
        return MD

    def reload_from_json(self, json):
        '''this function replaces all attributes of the Student
        '''
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
