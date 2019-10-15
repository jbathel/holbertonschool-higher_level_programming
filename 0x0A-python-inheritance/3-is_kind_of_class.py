#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Returns True if object is an instance of, or is an instance
    of a class that inherited from, the specified class
    """
    return isinstance(obj, a_class)
