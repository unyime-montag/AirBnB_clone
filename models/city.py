#!/usr/bin/env python3
""" class inherit from basemodel """
from models.base_model import BaseModel


class City(BaseModel):
        """ public class attribute """
        state_id = ""
        name = ""
