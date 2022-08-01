#!/usr/bin/python3
'''module for 1-my_list.py'''


class MyList(list):
    """class utilize list class"""

    def print_sorted(self):
        """print sorted list"""
        rez = list.copy(self)
        list.sort(rez)
        print(rez)
