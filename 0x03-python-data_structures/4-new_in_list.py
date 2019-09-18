#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        temp_list = my_list[:]
        if idx < 0 or idx > len(temp_list) - 1:
            return temp_list
        else:
            temp_list[idx] = element
            return temp_list
