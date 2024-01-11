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
