#!/usr/bin/python3
"""
Module defining a new class: FileStorage
This module handles the serialization and deserialization
of object instances to and from a JSON file.
"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage:
    """
    Class for serializing and deserializing object
    instances to and from a JSON file.

    Attributes:
        __file_path (str): Path to the JSON file (defaults to "file.json").
        __objects (dict): Dictionary storing instances in memory
        (key: class_name.id, value: instance).

    Methods:
        all(self): Returns the complete __objects dictionary.
        new(self, obj): Adds a new object to the __objects dictionary.
        save(self): Serializes the __objects
        dictionary to JSON format in a file.
        reload(self): Deserializes the JSON file content into object instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the complete __objects dictionary,
        exposing all stored instances.

        Caution:
            Exposing the entire dictionary might not be desirable
            depending on the application logic.
            Consider providing methods to retrieve specific instances
            or filter based on criteria.

        Example usage:
            >>> storage = FileStorage()
            >>> objects = storage.all()
            >>> for key, value in objects.items():
            ...     print(f"key: {key}, value: {value}")

        Returns:
            dict: Dictionary containing all stored instances,
            with keys formatted as "class_name.id".
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object (`obj`) to the `__objects` dictionary
        with a key formed by concatenating the object's class name
        and its ID (`"{}.{}"` format).

        Example usage:
            >>> user = User(email="example@email.com", password="password123")
            >>> storage = FileStorage()
            >>> storage.new(user)

        Arguments:
            obj (BaseModel): Instance of the `BaseModel` class
            or its derived classes.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the `__objects` dictionary to JSON format in a file.

        1. Creates a new dictionary (`new_dict`) to
        avoid modifying the original one.
        2. Iterates through `__objects` and calls the `to_dict()`
        method of each object to generate a
        serializable representation.
        3. Opens the JSON file (`__file_path`) in write
        mode (`"w"`) with UTF-8 encoding.
        4. Truncates the file content before writing
        (to avoid duplicates during successive saves).
        5. Dumps the `new_dict` content to the JSON file using `json.dump()`.

        Example usage:
            >>> storage = FileStorage()
            >>> storage.save()
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            file.truncate(0)
            json.dump(new_dict, file)

    def reload(self):
        """
        Deserializes the JSON file content into object instances.

        1. Tries to open the file in read mode (`"r"`) with UTF-8 encoding.
        2. On successful opening:
            - Loads the JSON content into `new_dict` using `json.load()`.
            - Iterates through `new_dict`:
                - Splits the key (`key`) to extract the
                class name and module name.
                - Dynamically imports the module using `__import__()`.
                - Retrieves the class using `getattr()`.
                - Creates a new instance of the class using
                its constructor (**kwargs) with the values from `new_dict`.
                - Stores the new instance in `FileStorage.__objects`
                with the original key.

        Example usage:
            >>> storage = FileStorage()
        """

        class_mapping = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        try:
            with open(self.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    obj_class_name = value.get("__class__")
                    if obj_class_name in class_mapping:
                        del value["__class__"]
                        obj_class = class_mapping[obj_class_name]
                        try:
                            obj = obj_class(**value)
                            self.new(obj)
                        except Exception as e:
                            print(f"Error loading data from JSON: {e}")
        except FileNotFoundError:
            pass
