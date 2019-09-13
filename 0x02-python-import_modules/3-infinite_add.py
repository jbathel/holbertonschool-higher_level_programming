#!/usr/bin/python3
import sys


def main():
    arguments = sys.argv
    arguments = arguments[1:]
    sum = 0
    for i in arguments:
        sum += int(i)
    print('{}'.format(sum))

if __name__ == '__main__':
    main()
