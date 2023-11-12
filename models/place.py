#!/usr/bin/python3
from models.base_model import BaseModel
class Place(BaseModel):
    number_rooms = 0
    number_bathrooms = 0
    city_id = ""
    user_id = ""
    name = ""
    latitude = 0.0
    longitude = 0.0
    description = ""
    max_guest = 0
    price_by_night = 0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
