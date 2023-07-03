#!/usr/bin/python3

"""
Module defines a Rectangle Class
"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instance initialisation method

        Args:
            width (int, optional): value of rectangle width. Defaults to 0.
            height (int, optional): value of rectangle height. Defaults to 0.
        """
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter method to access private attribute self.__width

        Returns:
            int: value of private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of private instance attribute self.__width

        Args:
            value (int): new value to set private attribute with

        Raises:
            TypeError: if value is not int
            ValueError: if value less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method to access private attribute self.__height

        Returns:
            int: value of private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of private instance attribute self.__height

        Args:
            value (int): new value to set private attribute with

        Raises:
            TypeError: if value is not int
            ValueError: if value less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of Rectangle

        Returns:
            int: product of self.width and self.height
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates perimeter of rectangle

        Returns:
            int: perimeter of Rectangle
        """
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """string representation of instance object

        Returns:
            str: representation of instance
        """
        obj_str = ""
        if not self.width or not self.height:
            return obj_str

        for col in range(self.height):
            for _ in range(self.width):
                obj_str += str(self.print_symbol)
            if col != (self.height - 1):
                obj_str += "\n"
        return obj_str

    def __repr__(self):
        """String representation of instance object

        Returns:
            str: representation of instance object
        """
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        """dunder method called when instance is deleted"""

        print("Bye rectangle...")
        if Rectangle.number_of_instances:
            Rectangle.number_of_instances -= 1
