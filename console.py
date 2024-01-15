#!/usr/bin/python3
""" The entry point of the command interpreter"""


import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
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

class HBNBCommand(cmd.Cmd):
    """ inheriting the Cmd class to customize it by ourself"""

    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'Amenity',
               'Place', 'City', 'State', 'Review']


    def onecmd(self, line):
        """Handles commands not explicitly defined in do_ methods."""
        match = re.match(r'^(?P<class_name>\w*)\.all\(\)$', line)
        if match:
            class_name = match.group('class_name')
            if not class_name:
                print("** class name missing **")
                return

            if class_name in class_list:
                self.do_all(class_name)
            else:
                print("** class doesn't exist **")
            return
        match = re.match(
            r'^(?P<class_name>\w*)\.show\(["\']?(?P<id>[\w-]*)["\']?\)$',
            line)
        if match:
            class_name = match.group('class_name')
            if not class_name:
                print("** class name missing **")
                return

            if class_name not in class_list:
                print("** class doesn't exist **")
                return
            else:
                isinstance_id = match.group('id')
                if not isinstance_id:
                    print("** instance id missing **")
                    return
                self.do_show(f"{class_name} {isinstance_id}")
                return
        match = re.match(
            r'^(?P<class_name>\w*)\.destroy\(["\']?(?P<id>[\w-]*)["\']?\)$',
            line)
        if match:
            class_name = match.group('class_name')
            if not class_name:
                print("** class name missing **")
                return

            if class_name not in class_list:
                print("** class doesn't exist **")
                return
            else:
                isinstance_id = match.group('id')
                if not isinstance_id:
                    print("** instance id missing **")
                    return
                self.do_destroy(f"{class_name} {isinstance_id}")
                return

        return super().onecmd(line)

    def do_EOF(self, line):
        """ EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """ Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Create new instance of a class given in {args}"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            Models = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
                      'Place': Place, 'City': City,
                      'State': State, 'Review': Review}
            new_inst = Models[arg]()
            print(new_inst.id)
            new_inst.save()

    def emptyline(self):
        """do nothing when empty line"""
        pass

    def do_show(self, line):
        """Displays information about an object"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")
            return

        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1]:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """destroy Deletes an objec at id """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")
            return

        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1]:
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Displays information about all objects"""
        if arg and arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        instances = []
        for key, value in all_objs.items():
            ob_name = value.__class__.__name__
            if arg and ob_name == arg:
                instances += [value.__str__()]
            else:
                instances += [value.__str__()]
        print(instances)

    def do_update(self, line):
        """Updates an object's attributes"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        elif args[0] not in HBNBCommand.classes:
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
