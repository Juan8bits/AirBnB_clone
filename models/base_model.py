#!/usr/bin/python3
""" This module define a class BaseModel """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Class BaseModel

    Attributes:
        id(UUID): Mandatory attribute. random UUID.
        created_at(datetime): Mandatory attribute. Creation date of the object.
        update_at(datetime): Mandatory attribute. Last update date of the obj.

    Methods:
        save(): Updates the public instance attribute updated_at with
                the current datetime.
        to_dict():  returns a dictionary containing all keys/values of
                    __dict__ of the instance.
        __str__: Informal representation of the object.
    """

    def __init__(self, *args, **kwargs):
        """ Initialized method class.

            if **kwars is not empty, create object with attributes given
            in kwargs. Otherwise, create id and created_at attributes.
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """Updates the public instance attribute updated_at with
           the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """ Informal representation for BaseModel """
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def to_dict(self):
        """ Method to returns a dictionary containing all keys/values of
           __dict__ of the instance.

        Return:
            Dictionary that containing all keys/values (attributes)
            of the object.
        """
        att = vars(self).keys()
        dic = {'__class__': self.__class__.__name__}
        for key in att:
            value = getattr(self, key)
            if key in ['created_at', 'updated_at']:
                value = getattr(self, key).isoformat()
            dic.update({key: value})
        return dic
