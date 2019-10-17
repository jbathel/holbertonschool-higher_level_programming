#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """Function that reads n lines of a text file and prints it to stdout"""
    with open(filename, encoding='utf-8') as filename:

        if nb_lines <= 0:
            print(filename.read(), end='')

        else:
            for line in range(nb_lines):
                print(filename.readlines(), end='')
