#!/usr/bin/python3
"""City Model
This module defines the `City` class, which represents 
a city and its attributes.
It inherits from the `BaseModel` class defined in 
`models.base_model.py`.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class Model that shows city imformation"""
    state_id = ""
    name = ""
