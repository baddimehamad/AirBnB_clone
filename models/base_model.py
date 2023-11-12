#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs['time_create'] = datetime.strptime(kwargs['time_create'],'%Y-%m-%dT%H:%M:%S.%f')
            kwargs['time_update'] = datetime.strptime(kwargs['time_update'],'%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.time_create = datetime.now()
            self.time_update = datetime.now()
            models.storage.new(self)


    def to_dict(self):
        the_new_dict = dict(self.__dict__)
        the_new_dict['time_create'] = self.__dict__['time_create'].isoformat()
        the_new_dict['time_update'] = self.__dict__['time_update'].isoformat()
        the_new_dict['__class__'] = self.__class__.__name__
        return (the_new_dict)
    
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()