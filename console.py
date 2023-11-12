#!/usr/bin/python3
'''Method Command Interpreter'''
import cmd
import shlex
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    allclasses = [
        "City",
        "Place",
        "Review",
        "State",
        "BaseModel",
        "User",
        "Amenity",

    ]

    def do_create(self, x):
        x = x.split()
        if len(x) == 0:
            print("you have a missing class name")
        elif x[0] not in HBNBCommand.allclasses:
            print("the class that you have called does not exist in the app")
        else:
            new_creation = eval(x[0] + '()')
            models.storage.save()
            print(new_creation.id)

    def do_show(self, x):
        text_name = x.split()
        if len(text_name) == 0:
            print("you have a missing class name")
        elif text_name[0] not in HBNBCommand.allclasses:
            print("the class that you have called does not exist in the app")
        elif len(text_name) == 1:
            print("the id in not found")
        else:
            obj = models.storage.all()
            key_value = text_name[0] + '.' + text_name[1]
            if key_value in obj:
                print(obj[key_value])
            else:
                print("nothing found")

    def do_destroy(self, z):
        z = z.split()
        x = models.storage.all()

        if len(z) == 0:
            print("you have a missing class name")
        elif z[0] not in HBNBCommand.allclasses:
            print("the class that you have called does not exist in the app")
        elif len(z) == 1:
            print("the id in not found")
        else:
            key_find = z[0] + '.' + z[1]
            if key_find in x.keys():
                x.pop(key_find, None)
                models.storage.save()
            else:
                print("the id in not found")

    def do_all(self, args):
        args = args.split()
        x = models.storage.all()
        new_list = []

        if len(args) == 0:
            for obj in x.values():
                new_list.append(obj.__str__())
            print(new_list)
        elif args[0] not in HBNBCommand.allclasses:
            print("the class that you have called does not exist in the app")
        else:
            for obj in x.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, args):
        x = models.storage.all()
        args = args.split(" ")

        if len(args) == 0:
            print("you have a missing class name")
        elif args[0] not in HBNBCommand.allclasses:
            print("the class that you have called does not exist in the app")
        elif len(args) == 1:
            print("the id in not found")
        elif len(args) == 2:
            print("the value passed not valid")
        elif len(args) == 3:
            print("value not found")
        else:
            found = args[0] + '.' + args[1]
            y = x.get(found, None)

            if not y:
                print("the id in not found")
                return

            setattr(y, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def check_class_name(self, name=""):
        if len(name) == 0:
            print("you have a missing class name")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        if len(name.split(' ')) == 1:
            print("the id in not found")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        if self.check_class_name(name):
            x = shlex.split(name)
            if x[0] in HBNBCommand.allclasses:
                if self.check_class_id(name):
                    key = x[0] + '.' + x[1]
                    return key
                else:
                    print("the class that you have called does not exist in the app")
                    return None

    def do_quit(self, x):
        return True

    def do_EOF(self, x):
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
