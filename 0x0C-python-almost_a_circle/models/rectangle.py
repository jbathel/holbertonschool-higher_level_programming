#!/usr/bin/python3
"""
This is a Rectangle Module for Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """x attribute"""
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """y attribute"""
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Area of Rectangle"""
        return (self.__width) * (self.__height)

    def display(self):
        """Print Rectangle"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                print(' ', end='')
            for i in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """Method to represent Rectangle Class"""
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Method to update attributes of instance"""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)

        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Method to create dictionary of attributes"""
        dictionary = {'id': self.id, 'width': self.__width,
                      'height': self.__height, 'x': self.__x, 'y': self.__y}
        return dictionary
