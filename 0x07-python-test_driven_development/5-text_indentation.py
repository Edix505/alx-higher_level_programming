#!/usr/bin/python3
'''do stuff to strings'''


def text_indentation(text):

    if type(text) is not str:
        raise TypeError('text must be a string')

    first_idx = 0
    for idx, char in enumerate(text):
        if char == '.' or char == '?' or char == ':':
            if (idx + 1) == len(text):
                tamp_str = text[first_idx:]
            else:
                tamp_str = text[first_idx:idx + 1]
            first_idx = idx + 1
            print(tamp_str.strip())
            print()
            continue

        if idx == len(text) - 1:
            tamp_str = text[first_idx:]
            print(tamp_str.strip())
