#!/usr/bin/python3
#Function that returns peak element of an array
def find_peak(list_of_integers):
"""Function that returns peak element of given array"""
    if (list_of_integers is NULL):
        return NULL

Binary Search
1. Initialize start = 0, end = array.length - 1
    start = list_of_integers[0]
    end = len(list_of_integers) - 1

2. Repeat the following steps till peak element is found:
    while(start <= end):
    a. Find mid = (start + end)/2
        mid = (start + end) / 2
    b. If mid is peak element, return array[mid]
        if mid >= mid - 1 and >= mid + 1
            return mid
    c. If array[mid - 1] > array[mid], find peak in left half of array
        set end = mid - 1
    d. Else find peak in right half of array
        set start = mid + 1
