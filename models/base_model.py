#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """ Represents a Base model class """

    def __init__(self, *args, **kwargs):
        """ Instantiation
        """

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        setattr(self, k, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, k, v)


    def __str__(self):
        """ Class format """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """ Update the 'update_at' attribute"""
        self.updated_at = datetime.now()
        storage.save()

    
    def to_dict(self):
        """ Turn attributes to dictionary object
        Return: Dictionary object
        """
        dict_rep = self.__dict__.copy()
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.created_at.isoformat()
        dict_rep['__class__'] = self.__class__.__name__

        return dict_rep
