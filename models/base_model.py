#!/usr/bin/python3
"""creating a class BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base model class"""
    def __init__(self, *args, **kwargs):
        """initialize instance"""
        if (kwargs is not None and len(kwargs) != 0):
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """return string representation of instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at to current
        datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict