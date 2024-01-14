#!/usr/bin/python3

""" Place class module that is inhirited from
BaseModel to create a new Place objects
while  inheriting all properties of baseModel
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Place class inhirted from BaseModel class
    with sevral new public atrr as
    str and int
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
