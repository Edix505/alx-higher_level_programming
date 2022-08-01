#!/usr/bin/python3
'''module 100-my_int.py'''


class MyInt(int):
    '''funky class'''
    def __eq__(self, other):
        ''' eq type method'''
        if int.__eq__(self, other):
            return False
        return True

    def __ne__(self, other):
        '''ne type method'''
        if int.__ne__(self, other):
            return False
        return True
