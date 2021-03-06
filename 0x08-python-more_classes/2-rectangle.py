#!/usr/bin/python3
class Rectangle:
    """A simple Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize attributes width and height"""
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    def area(self):
        return (self.__height) * (self.__width)

    def perimeter(self):
        if self.__width and self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2
