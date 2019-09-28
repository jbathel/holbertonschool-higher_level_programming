#!/usr/bin/python3
def weight_average(my_list=[]):
    return  [[(i + i for i in row) / range(len(my_list))] for row in my_list]

for row in my_list:
    for col in my_list:

