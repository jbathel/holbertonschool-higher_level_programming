#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    digit = (abs(number) % 10) * -1
elif number > 0:
    digit = number % 10

print('Last digit of {} is {} and is '.format(number, digit), end="")
if digit == 0:
    print('0'.format(digit))
elif digit < 6 and digit != 0:
    print('less than 6 and not 0'.format(digit))
elif digit > 5:
    print('greater than 5'.format(digit))
