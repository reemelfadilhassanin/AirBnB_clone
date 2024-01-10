#!/usr/bin/python3
""" The entry point of the command interpreter"""

import cmd
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
