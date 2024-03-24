#!/user/bin/python3
"""Place module """
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a Place class """
    city_id = ""  # City class id
    user_id = ""  # User class id
    name = ""  # Name of place
    description = ""  # Description of place
    number_rooms = 0  # Number of rooms in place
    number_bathrooms = 0  # Number of bathrooms in place
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = ""
