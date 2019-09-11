#!/usr/bin/python3
for i in range(0, 99):
    if i < 98:
        print('{0:02d}'.format(int(i)), end=", ")
    else:
        print('{}'.format(int(i)))
