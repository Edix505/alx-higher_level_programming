#!/usr/bin/python3
def no_c(my_string):
    a_string = ""
    for a in range(len(my_string)):
        if my_string[a] != 'c' and my_string[a] != 'C':
            a_string += my_string[a]
    return a_string
