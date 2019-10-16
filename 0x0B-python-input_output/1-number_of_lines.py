#!/usr/bin/python3
def number_of_lines(filename=""):
    with open("my_file_0.txt", encoding="utf-8") as filename:
        lineNum = 0
        while True:
            line = filename.readline()
            if not line:
                break
            lineNum += 1
        return lineNum
