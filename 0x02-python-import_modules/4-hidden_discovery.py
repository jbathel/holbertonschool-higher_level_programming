#!/usr/bin/python3
import hidden_4


def main():
    for names in dir(hidden_4):
        if not names.startswith('__'):
            print(names)

if __name__ == '__main__':
    main()
