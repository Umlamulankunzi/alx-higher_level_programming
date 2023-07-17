#!/usr/bin/python3


"""Module defining the class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialises new instance of Square Class

        Args:
            size (int): value of side of Square
            x (int, optional): value of x. Defaults to 0.
            y (int, optional): value of y. Defaults to 0.
            id (int, optional): value of id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for attribute size.

        Returns:
            int: size of one side of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Attribute setter for size.

        Args:
            value (int): new value for size.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width <= 0.
        """
        self.validate_int_arg("width", value)

        self.width = value
        self.height = value

    def __str__(self):
        info = {
            "id": self.id, "x": self.x, "y": self.y, "width": self.width,
            "height": self.height
        }
        return "[Square] ({id}) {x}/{y} - {width}".format(**info)

    def update(self, *args, **kwargs):
        """Updates instance attributes"""

        if len(args) != 0 and args is not None:
            args_attr = ("id", "size", "x", "y")
            for arg_name, arg_val in zip(args_attr, args):
                setattr(self, arg_name, arg_val)
        else:
            for arg_name, arg_val in kwargs.items():
                setattr(self, arg_name, arg_val)

    def to_dictionary(self):
        """returns dictionary attributes of object

        Returns:
            dict: dict of instance attributes of object
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
