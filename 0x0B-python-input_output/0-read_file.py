#!/usr/bin/python3
def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout"""
    with open("my_file_0.txt", encoding="utf-8") as filename:
        print(filename.read())
