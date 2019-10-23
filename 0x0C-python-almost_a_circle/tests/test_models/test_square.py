#!/usr/bin/python3
"""
Unittest for Square Size
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareSize(unittest.TestCase):
    """Test Square Size Method"""
    def test_size(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
