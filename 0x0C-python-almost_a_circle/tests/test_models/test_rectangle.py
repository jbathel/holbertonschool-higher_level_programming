#!/usr/bin/python3
"""
Unittesting for Class - Base
models/base.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


class RectangleTest(unittest.TestCase):
    """Class Base unittests"""

    def test_check_id(self):
        """Test if id of Rectangle increments"""
        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(2, 10)
        self.assertEqual(r3.id, 3)

    def test_check_input_id(self):
        """Test if input id gets set"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_check_width(self):
        """Test width set of rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)

        r3 = Rectangle(5, 2, 0, 0, 12)
        self.assertEqual(r3.width, 5)

    def test_check_width_TypeError_01(self):
        """Test TypeError for width in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'width must be an integer',
            Rectangle,
            'string', 2, 0, 0, 12
        )

    def test_check_width_TypeError_02(self):
        """Test TypeError for width in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'width must be an integer',
            Rectangle,
            [6, 4, 9, 9], 2, 0, 0, 12
        )

    def test_check_width_ValueError(self):
        """Test TypeError for width in Rectangle"""
        self.assertRaisesRegex(
            ValueError,
            'width must be > 0',
            Rectangle,
            -1, 2, 0, 0, 12
        )

    def test_check_height(self):
        """Test height of """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.height, 10)

        r3 = Rectangle(5, 3, 0, 0, 12)
        self.assertEqual(r3.height, 3)

    def test_check_height_TypeError_01(self):
        """Test TypeError for height in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'height must be an integer',
            Rectangle,
            2, 'string', 0, 0, 12
        )

    def test_check_height_TypeError_02(self):
        """Test TypeError for height in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'height must be an integer',
            Rectangle,
            3, [1, 2, 3, 4], 0, 0, 12
        )

    def test_check_height_ValueError(self):
        """Test TypeError for height in Rectangle"""
        self.assertRaisesRegex(
            ValueError,
            'height must be > 0',
            Rectangle,
            1, -2, 0, 0, 12
        )

    def test_check_x(self):
        """Test x of rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)

        r2 = Rectangle(2, 10, 6)
        self.assertEqual(r2.x, 6)

        r3 = Rectangle(5, 2, 3, 9, 12)
        self.assertEqual(r3.x, 3)

        r4 = Rectangle(5, 2, 0, 3, 12)
        self.assertEqual(r4.x, 0)

    def test_check_x_TypeError_01(self):
        """Test TypeError for x in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'x must be an integer',
            Rectangle,
            4, 2, 'string''', 0, 12
        )

    def test_check_x_TypeError_02(self):
        """Test TypeError for x in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'x must be an integer',
            Rectangle,
            4, 2, [1, 2, 3, 4], 0, 12
        )

    def test_check_x_ValueError(self):
        """Test ValueError for x in Rectangle"""
        self.assertRaisesRegex(
            ValueError,
            'x must be >= 0',
            Rectangle,
            4, 2, -1, 0, 12
        )

    def test_check_y(self):
        """Test y of rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10, 6, 4)
        self.assertEqual(r2.y, 4)

        r3 = Rectangle(5, 2, 3, 9, 12)
        self.assertEqual(r3.y, 9)

        r4 = Rectangle(5, 2, 3, 0, 12)
        self.assertEqual(r4.y, 0)

    def test_check_y_TypeError_01(self):
        """Test TypeError for y in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'y must be an integer',
            Rectangle,
            4, 2, 0, 'string', 12
        )

    def test_check_y_TypeError_02(self):
        """Test TypeError for y in Rectangle"""
        self.assertRaisesRegex(
            TypeError,
            'y must be an integer',
            Rectangle,
            4, 2, 0, [1, 2, 3, 4], 12
        )
    def test_check_y_TypeError_(self):
        """Test TypeError for y in Rectangle"""
        self.assertRaisesRegex(
            ValueError,
            'y must be >= 0',
            Rectangle,
            4, 2, 0, -6, 12
        )

    def test_to_dictionary(self):
        """Test conversion to dictionary"""
        r = Rectangle(1, 1, 1, 1, 1)
        d = {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}
        self.assertEqual(r.to_dictionary(), d)
        r.my_fun_new_attr = 42
        self.assertEqual(r.to_dictionary(), d)
