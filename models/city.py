#!/usr/bin/python3
""" Class City that inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class to create city Object """
    state_id = ""
    name = ""
