#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Last digit of 4205 is 5 and is last_digitess than 6 and not 0
# Last digit of -9200 is 0 and is 0
# Last digit of 5247 is 7 and is greater than 5
# isolast_digitate last digit

last_digit = number%10

if number < 0:
    last_digit = last_digit*-1
if last_digit == 0:
    print('Last digit of {} is {} and is 0'.format(number, last_digit))
elif last_digit < 6:
    print('Last digit of {} is {} and is less than 6 and not 0'.format(number, last_digit))
elif last_digit > 5:
    print('Last digit of {} is {} and is greater than 5'.format(number, last_digit))
