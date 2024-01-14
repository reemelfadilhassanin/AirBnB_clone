#!/usr/bin/python3

""" City  class module that is inhirited from
BaseModel to create a new city objects
while inheriting all properties of baseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """City class inhirted from BaseModel class with two
    public attrr
    state_id and name both are empty str
    """
    state_id = ""
    name = ""
