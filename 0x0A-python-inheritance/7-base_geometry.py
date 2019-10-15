#!/usr/bin/python3
class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        """Area attribute"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int) is False:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
