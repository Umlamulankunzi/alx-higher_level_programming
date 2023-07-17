#!/usr/bin/python3


"""Module defining the class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectange class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises new instance of Rectangle Class

        Args:
            width (int): value of width
            height (int): value of height
            x (int, optional): value of x. Defaults to 0.
            y (int, optional): value of y. Defaults to 0.
            id (int, optional): value of id. Defaults to None.
        """
        super().__init__(id)
        # setters method calls validation methods
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def validate_int_arg(name, value):
        """validates instance attributes whether they are valid.

        Except for the id atrribute.

        Args:
            name (str): name of attribute to validate
            value (int): value of attribute

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0 and if name equal to "width" or "height"
            ValueError: if value < 0 and if name equal to "x" or "y"
        """
        if not isinstance(value, (int)):
            raise TypeError("{} must be an integer".format(name))
        if name in ("width", "height"):
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        elif name in ("x", "y"):
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Getter method for private instance attribute self.__width

        Returns:
            int: value of private instance attribute self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for private instance attribute self.__width

        Args:
            value (int): new value to set private instance attribute
        """
        self.validate_int_arg("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter method for private instance attribute self.__height

        Returns:
            int: value of private instance attribute self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for private instance attribute self.__height

        Args:
            value (int): new value to set private instance attribute
        """
        self.validate_int_arg("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for private instance attribute self.__x

        Returns:
            int: value of private instance attribute self.__x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for private instance attribute self.__x

        Args:
            value (int): new value to set private instance attribute
        """
        self.validate_int_arg("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for private instance attribute self.__y

        Returns:
            int: value of private instance attribute self.__y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for private instance attribute self.__y

        Args:
            value (int): new value to set private instance attribute
        """
        self.validate_int_arg("y", value)
        self.__y = value

    def area(self):
        """Calculates area of Rectangle Instance

        Returns:
            int: area
        """
        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance with chararcter #"""

        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """Updates instance attributes"""

        if len(args) != 0 and args is not None:
            args_attr = ("id", "width", "height", "x", "y")
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
        return {
            "id": self.id, "width": self.width, "height": self.height,
            "x": self.x, "y": self.y}

    def __str__(self):
        info = {
            "id": self.id, "x": self.x, "y": self.y, "width": self.width,
            "height": self.height
        }
        return "[Rectangle] ({id}) {x}/{y} - {width}/{height}".format(**info)
