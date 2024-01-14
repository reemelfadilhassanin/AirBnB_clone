#!/usr/bin/python3
""" The entry point of the command interpreter"""

import cmd
import re
import json
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review

try:
    import gnureadline as readline
except ImportError:
    import readline

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')


class_list = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place
}


def normalize_value(value):
    """function to normalize values"""
    if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
        return int(value)
    elif value.startswith('"') and not value.endswith('"'):
        return value.stri('"')

    try:
        return float(value)
    except (ValueError, Exception):

        return value.strip('"')

    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    else:
        return value.strip('"')


class HBNBCommand(cmd.Cmd):
    """ inheriting the Cmd class to customize it by ourself"""
    prompt = '(hbnb) '

    def do_create(self, args):
        """Create new instance of a class given in {args}"""
        if args:
            if args not in class_list:
                print("** class doesn't exist **")
                return
            args = args.split()
            new_inst = class_list[args[0]]()
            new_inst.save()
            print(new_inst.id)
        else:
            print("** class name missing **")

    def do_show(self, args):
        """Prints the string representation of an
        instance based on the class name and id"""
        if args:
            flag = 0
            words = args.split()
            if len(words) < 2:
                print("** instance id missing **")
                return
            if words[0] not in class_list:
                print("** class doesn't exist **")
                return

            all_obj = storage.all()
            instance_key = "{}.{}".format(words[0], words[1])
            if instance_key in all_obj:
                print(all_obj[instance_key])
            else:
                print("** no instance found **")
                return
        else:
            print("** class name missing **")
            return

    def do_destroy(self, args):
        """Deletes an instance based on class name and id"""
        if args:
            flag = 0
            words = args.split()
            if len(words) < 2:
                print("** instance id missing **")
                return
            if words[0] not in class_list:
                print("** class doesn't exist **")
                return

            all_obj = storage.all()
            instance_key = "{}.{}".format(words[0], words[1])

            for key, obj in all_obj.items():
                if key.split('.')[1] == words[1]:
                    del all_obj[instance_key]
                    storage.save()
                    flag = 1
                    break

            if flag == 0:
                print("** no instance found **")

        else:
            print("** class name missing **")

    def do_all(self, args):
        """Prints all string representation of all instances"""
        words = args.split()
        class_name = None
        if words and words[0] not in class_list:
            print("** class doesn't exist **")
            return
        if words:
            class_name = words[0]
        instances = storage.all()
        instances_list = []
        for instance_key in instances:
            if class_name is None or instance_key.startswith(class_name):
                instances_list.append(str(instances[instance_key]))
        print(instances_list)

    def do_update(self, args):
        """Updates an instance on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        class_name, *atrr_args = args.split()
        if class_name not in class_list:
            print("** class doesn't exist **")
            return

        if not atrr_args:
            print("** instance id missing **")
            return

        all_obj = storage.all()
        instance_key = "{}.{}".format(class_name, atrr_args[0])

        if instance_key not in all_obj:
            print("** no instance found **")
            return

        if len(atrr_args) == 1:
            print("** attribute name missing **")
            return

        instance = all_obj[instance_key]

        if atrr_args[1].startswith('{') and atrr_args[-1].endswith('}'):
            try:
                str_json = ' '.join(args[2:])
                value_dict = json.loads(str_json)

                for key, value in value_dict.items():
                    setattr(instance, key, value)
            except (json.JSONDecodeError, Exception) as e:
                print("json.JSONDecodeError ", str(e))
                pass

        else:
            if len(atrr_args) == 2:
                print("** value missing **")
                return

            attr_name = atrr_args[1].strip('"')
            value = ' '.join(atrr_args[2:]).strip('"')
            setattr(instance, attr_name, normalize_value(value))

        instance.updated_at = datetime.now()
        instance.save()

    def do_quit(self, args):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """ EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty lines."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
