#!/usr/bin/python3


"""Defines class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry. """

    def area(self):
        """Area function.

        Raises:
            Exception: if area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value.

        Args:
            name (str): name of object.
            value (int): value of property.

        Raises:
            TypeError: if value is not an int.
            ValueError: if value less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
