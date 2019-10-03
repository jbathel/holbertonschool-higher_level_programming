#!/usr/bin/python3
class Node:
    "Instantiation of SinglyLinkedList Class"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    """ """
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    """ """
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if self.__next_node != None or self.__next_node != type(Node):
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value

class SinglyLinkedList:
    "Instantiation of SinglyLinkedList Class"""
    def __init__(self, head=None):
        self.head = head

    def sorted_insert(self, value):
        new_node = Node(value)
        new_node.__next_node = self.__head
        self.__head = new_node

#check if value is < or > head

#if true add node after head

#if false add node before head



