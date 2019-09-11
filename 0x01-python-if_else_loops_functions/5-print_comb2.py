#!/usr/bin/python3
for i in range(0, 99):
    if i < 10:
        print('{0:02d}'.format(int(i)), end=", ")
    elif i > 10 and i < 98:
        print('{}'.format(int(i)), end=", ")
    else:
        print('{}'.format(int(i)))
