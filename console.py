#!/usr/bin/python3
""" Console Module """

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """Represents a console"""

    prompt = '(hbnb) '  # shell prompt
    list_class = ['BaseModel', 'User', 'Place',
                  'City', 'Amenity', 'State', 'Review']

    def do_EOF(self):
        """EOF command to exit program"""
        return True

    def do_quit(self, line):
        """Quit command to exit program """
        return True

    def emptyline(self):
        """ Do nothing """
        pass

    def do_create(self, type_model):
        """ Create user """

        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place':
                   Place, 'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            model = dct[type_model]()
            print(model.id)
            model.save()

    def do_show(self, arg):
        """ Prints string representation of instance """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')
        model_name = args[0]
        if model_name not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for k, v in all_objs.items():
                ob_name = v.__class__.__name__
                ob_id = v.id
                if ob_name == model_name and ob_id == args[1].strip('"'):
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Delete an instance """

        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')
        model_name = args[0]
        if model_name not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for k, v in all_objs.items():
                ob_name = v.__class__.__name__
                ob_id = v.id
                if ob_name == model_name and ob_id == args[1].strip('"'):
                    del v
                    del storage._FileStorage__objects[k]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Delete instance """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(" ")
        model_name = args[0]
        if model_name not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for k, v in all_objs.items():
                ob_name = v.__class__.__name__
                if ob_name == model_name:
                    list_instances += [v.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """ Update instance """

        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        obj_id = args[1].strip('"')

        if class_name not in HBNBCommand.list_class:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        found_instance = None

        for k, objc in all_objs.items():
            if type(objc).__name__ == class_name and objc.id == obj_id:
                found_instance = objc
                break

            if found_instance:
                if len(args) < 4:
                    print("** attribute name missing **")
                    return
            attr_name = args[2]
            attr_value = args[3]
            setattr(found_instance, attr_name, attr_value)
            storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
