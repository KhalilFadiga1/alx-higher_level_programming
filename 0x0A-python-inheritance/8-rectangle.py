#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initialise a new Rectangle.

    Args:
        width (int): The width of the new Rectangle.
        height (int): The height of the rectangle.
    """
    self.integer_validator("width", width)
    self.__width = width
    self.integer_validator("height", height)
    self.__height = height
