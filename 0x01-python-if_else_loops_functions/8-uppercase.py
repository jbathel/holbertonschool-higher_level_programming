#!/usr/bin/python3
def uppercase(str):
    for c in str:
        flag = 0
        if ord(c) >= 97 and ord(c) <= 122:
            flag = 32
        print('{:c}'.format(ord(c) - flag), end="")
    print()
