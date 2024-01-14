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
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



class_list = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review
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
        if not args:
            print("** class name missing **")
        elif args not in class_list:
            print("** class doesn't exist **")
        else:
            new_inst = class_list[args]()
            print(new_inst.id)
            new_inst.save()

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
        args = args.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        elif args[0] not in class_list:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")
            return

        else:
            class_name = args[0]
            instance_id = args[1]

            objects = storage.all()
            key = f"{class_name}.{instance_id}"

            if key not in objects:
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return

            elif len(args) < 4:
                print("** value missing **")
                return

            value = args[3].replace('"', '')

            for key, objc in objects.items():
                ob_id = objc.id
                if ob_id == args[1]:
                    setattr(objc, args[2], value)
                    storage.save()
                    storage.reload()

    def do_quit(self, args):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """ EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty lines."""
        pass

    def help_help(self):
        """Displays the help message"""
        print("Help:\nhow to use\n\tcreate\tUsage: create <class name>\
              \n\n\tshow\tUsage: show <class name> <ID>\
              \n\n\tdestroy\tUsage: destroy <class name> <ID>\
              \n\n\tall\tUsage: all <class name > || all\
              \n\n\tupdate\tUsage: update <class name> <id> \
               <attribute name> <attribute value>")
        return

    def help_EOF(self):
        """Exits the command interpreter"""
        print("EOF Quit the command interpreter\n")

    def help_quit(self):
        """help Quit info """
        print("Quit the command interpreter\n")

    def help_create(self):
        """help Creates a new object"""
        print("Usage: create <class name>")
        return

    def help_show(self):
        """help Displays information about an object"""
        print("Usage: show <class name> <ID>")
        return

    def help_destroy(self):
        """help destroy obj at ID"""
        print("Usage: destroy <class name> <ID>")
        return

    def help_all(self):
        """Help Displays information about all objects"""
        print("all <class name > || all")

    def help_update(self):
        """help Update message"""
        print("Usage: update <class name> <id> \
              <attribute name> \"<attribute value>\"")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
