#!/usr/bin/python3

"""module defining base class"""

import json
import os.path
import csv
import turtle


class Base:
    """ Base class that is parent class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialise new instanve if class

        Args:
            id (int): id of instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries.

        Returns:
            str: json formatted string representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Converts json str to python objects

        Args:
            json_string (str): json formatted str

        Returns:
            list: python object
        """
        if json_string is None or len(json_string) == 0:
            return []
        return(json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): Base child class object instances
        """
        filename = "{}.json".format(cls.__name__)
        dict_of_obj_list = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                dict_of_obj_list.append(obj.to_dictionary())

        list_objs_str = cls.to_json_string(dict_of_obj_list)

        with open(filename, 'w') as file:
            file.write(list_objs_str)

    @classmethod
    def create(cls, **dictionary):
        """Returns new class instance, with attributes set using dictionary.

        Args:
            dictionary (dict): dictionary with values of new instance attrs.
            cls (any): class.

        Returns:
            (Square, Rectangle): new instance.
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances.

        Args:
            cls (any): class.

        Returns:
            list: list of instances.
        """
        filename = "{}.json".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            inst_list_str = file.read()

        inst_list_obj = cls.from_json_string(inst_list_str)
        list_ins = []

        for obj_dict in inst_list_obj:
            list_ins.append(cls.create(**obj_dict))

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list of Rectangles or Square objects in csv.

        Args:
            cls (Rectangle, Square): class.
            list_objs (list): list of objects.
        """
        filename = "{}.csv".format(cls.__name__)

        with open(filename, 'w', newline="") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])

            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a list of Rectangles or Squares objects in csv.

        Args:
            cls (Rectangle, Square): class.
        """
        filename = "{}.csv".format(cls.__name__)
        obj_lists = []

        try:
            with open(filename, 'r') as file:
                csv_reader = csv.reader(file)
                for line in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {
                            "id": int(line[0]), "width": int(line[1]),
                            "height": int(line[2]), "x": int(line[3]),
                            "y": int(line[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {
                            "id": int(line[0]), "size": int(line[1]),
                            "x": int(line[2]), "y": int(line[3])}
                    obj = cls.create(**dictionary)
                    obj_lists.append(obj)

        except (ValueError, FileNotFoundError, IOError, csv.Error):
            pass
        return obj_lists

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Methid to draw squares and rectangles using turtle"""

        # turtle.setup(width=800, height=600)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.pensize(5)

        # Create a turtle object
        my_turtle = turtle.Turtle()

        # Draw a square
        for square in list_squares:
            for _ in range(4):
                my_turtle.forward(square.size)
                my_turtle.right(90)
            turtle.penup()
            turtle.forward(square.size + 10)
            turtle.pendown()

        # Draw Rectangle
        for rectangle in list_rectangles:

            for _ in range(2):
                my_turtle.forward(rectangle.width)
                my_turtle.right(90)
                my_turtle.forward(rectangle.height)
                my_turtle.right(90)  # Turn right by 90 degrees

        turtle.done()
