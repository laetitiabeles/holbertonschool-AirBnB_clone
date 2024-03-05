#!/usr/bin/python3
""" Base Model creation """

from datetime import datetime
import uuid


class BaseModel:
    """ Base Model class """
    def __init__(self, *args, **kwargs):
        """ Initialization instance attributes
        Args:
             args: set of arguments
             kwargs: set of arguments with keywords
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Base Model string """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Base Model save """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Base Model dictionart """
        data_dict = self.__dict__.copy()
        data_dict['__class__'] = self.__class__.__name__
        data_dict['created_at'] = self.created_at.isoformat()
        data_dict['updated_at'] = self.updated_at.isoformat()
        return data_dict
