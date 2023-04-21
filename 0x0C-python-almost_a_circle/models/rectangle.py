#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    """
    Represents a rectangle.

    Attributes:
    - id (int): The id of the rectangle.
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
    - x (int): The x-coordinate of the rectangle.
    - y (int): The y-coordinate of the rectangle.

    Methods:
    - __init__(self, width, height, x=0, y=0, id=None): Initializes a new instance of the Rectangle class.
    - width(self): Gets the width of the rectangle.
    - width(self, value): Sets the width of the rectangle to the specified value.
    - height(self): Gets the height of the rectangle.
    - height(self, value): Sets the height of the rectangle to the specified value.
    - x(self): Gets the x-coordinate of the rectangle.
    - x(self, value): Sets the x-coordinate of the rectangle to the specified value.
    - y(self): Gets the y-coordinate of the rectangle.
    - y(self, value): Sets the y-coordinate of the rectangle to the specified value.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int): The x-coordinate of the rectangle (default: 0).
        - y (int): The y-coordinate of the rectangle (default: 0).
        - id (int): The id of the rectangle (default: None).
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle to the specified value.

        Args:
        - value (int): The new width of the rectangle.
        """
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle to the specified value.

        Args:
        - value (int): The new height of the rectangle.
        """
        self.__height = value

    @property
    def x(self):
        """
        Gets the x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the rectangle to the specified value.

        Args:
        - value (int): The new x-coordinate of the rectangle.
        """
        self.__x = value

    @property
    def y(self):
        """
        Gets the y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the rectangle to the specified value.

        Args:
        - value (int): The new y-coordinate of the rectangle.
        """
        self.__y = value
