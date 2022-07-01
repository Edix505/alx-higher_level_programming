#!/usr/bin/python3

if __name__ == "__main__":
import 4_hidden


def principal():
    for i in dir(4_hidden):
        if not (i[0] == '_' and i[1] == '_'):
            print(i)

     principal()
