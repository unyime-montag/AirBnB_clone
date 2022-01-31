#!/usr/bin/env python3
""" class inherit from basemodel """
from models.base_model import BaseModel


class Amenity(BaseModel):
        """ public class attribute """
        place_id = ""
        user_id = ""
        text = ""
