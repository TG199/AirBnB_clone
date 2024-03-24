#!/user/bin/python3
""" City Module """
from models.base_model import BaseModel


class City(BaseModel):
    """ Represents a city class """

    state_id = ""  # State id
    name = ""  # Name of city
