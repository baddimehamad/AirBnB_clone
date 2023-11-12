#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
class FileStorage():
    __file_path = "f.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        dictioner = {}
        for key, value in FileStorage.__objects.items():
            dictioner[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(dictioner, my_file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                dictioner = json.load(my_file)

            for key, value in dictioner.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
