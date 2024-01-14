#!/usr/bin/python3

""" Review Class module that is inhirited from
BaseModel to create a new review objects
while inheriting all properties of baseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inhirted from BaseModel class
    with three more atrr
    place_id and user_id
    text for description
    """
    place_id = ""
    user_id = ""
    text = ""
