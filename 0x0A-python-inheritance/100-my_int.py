#!/usr/bin/python3
class MyInt(int):
    """MyInt Class"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
