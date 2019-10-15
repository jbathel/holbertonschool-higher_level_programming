#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Returns True if object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    """
    return isinstance(obj, a_class) != a_class
