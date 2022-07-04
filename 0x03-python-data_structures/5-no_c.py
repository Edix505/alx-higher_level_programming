#!/usr/bin/python3
def no_a(my_string):
    a_string = ""
    for a in my_string:
        if a != 'a' and a != 'A':
            a_string += a
    return a_string
