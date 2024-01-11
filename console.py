#!/usr/bin/python3
""" The entry point of the command interpreter"""

import cmd
import re
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
try:
    import gnureadline as readline
except ImportError:
    import readline
from models import storage
from models.base_model import BaseModel
from models.user import User

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')


class HBNBCommand(cmd.Cmd):
    """ inheriting the Cmd class to customize it by ourself"""
    prompt = ('(hbnb) ')

    def do_quit(self, args):
        """ Quit command to exit the program"""
        exit()

    def do_EOF(self, args):
        """ EOF command to exit the program"""
        exit()

    def do_emptyline(self, line):
        """Do nothing on empty lines."""
        pass

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        new_instance = storage.classes()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if not arg or args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        class_name = args[0]
        all_objs = storage.all()
        objects = [str(obj) for obj in all_objs.values()
                   if obj.__class__.__name__ == class_name]
        print(objects)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        value = args[3]
        obj = all_objs[key]
        setattr(obj, attribute_name, value)
        storage.save()

	def do_create(self, args):
		"""Create new instance of a class given in {args}"""
		if args:
			if args == "BaseModel":
				new_inst = BaseModel()
				new_inst.save()
				print(new_inst.id)
			else:
				print("** class doesn't exist **")
		else:
			print("** class name missing **")

	def do_show(self, args):
		"""Prints the string representation of an instance based on the class name and id"""
		if args:
			words = args.split()
			if words[0] == "BaseModel":
				if len(words) != 2:
					print("** instance id missing **")
				else:
					all_obj = FileStorage.all(BaseModel)
					for obj in all_obj:
						if obj.id == words[1]:
							print(BaseModel.to_dict(obj))
						print(obj.id)
					print("** no instance found **")
				
			else:
				print("** class doesn't exist **")
			
		else:
			print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
