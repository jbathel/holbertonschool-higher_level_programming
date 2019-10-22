#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size"""
        return self.width

    @size.setter
    def size(self, value):
        """Size"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        return ('[Square] ({}) {}/{} - {}'.format
                (self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)

        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        dictionary = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dictionary
