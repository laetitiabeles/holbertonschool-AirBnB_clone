#!/usr/bin/python3
"""Amenity Model"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class Model that shows amenity imformation
    Amenity class representing an amenity object with the following attributes:

    - name (str): The name of the amenity.

    Inherits from the `BaseModel` class, providing common attributes and methods
    for managing object persistence."""
    name = ""
