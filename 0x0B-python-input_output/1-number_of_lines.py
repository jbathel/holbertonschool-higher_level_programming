#!/usr/bin/python3
def number_of_lines(filename=""):
    """Function that returns the number of lines of a text file"""
    with open("my_file_0.txt", encoding="utf-8") as filename:
        lineNum = 0
        while True:
            line = filename.readline()
            if not line:
                break
            lineNum += 1
        return lineNum
