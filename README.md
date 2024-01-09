# AirBnB clone
<p align="center">

![ICONE](hbnb.PNG)



### Welcome to the AirBnB clone project!

> This is a team project full-stack web application that mimics the functionality of the popular online book. 

The primary tasks include:

- Implementing a parent class (BaseModel) responsible for initializing, serializing, and deserializing instances.
- Create a flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Creating classes (User, State, City, Place, etc.) that inherit from BaseModel.

## What’s a command interpreter?
A command interpreter is a tool that allows to manage objects for the AirBn website.
#### Main functionality of this command interpreter:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### How to start it:
To run the program you need Python 3 installed in your computer and then execute the following commands
in the terminal:

- Clone this repository: git clone "https://github.com/reemelfadilhassanin/AirBnB_clone
- Go into the directory: cd AirBnB_clone
- The cmd should work in both interactive and non - interactive mode  like a shell.

## Usage:

| Commands | Uses |
| --- | --- |
| Create | create the new object like id|
| Update | update the attribute of object |
| Help | display the help page of command |
| All | display all attributes of objects of class |
| Show | show information of object|
| Quite | exit from the cmd|
| Destory | destory the object|


## Examples of use
**Interactive mode**
---
> $ ./console.py
(hbnb) help
Documented commands (type help <topic>):
=======================================

> EOF  help  quit

> (hbnb) 
> (hbnb) 
> (hbnb) quit
> $

**Non - Interactive mode**
---
> $ echo "help" | ./console.py

> (hbnb)

> Documented commands (type help <topic>):
========================================

> EOF  help  quit

> (hbnb) 
> $

> $ cat test_help

> help

> $

> $ cat test_help | ./console.py

> (hbnb)

> Documented commands (type help <topic>):
========================================

> EOF  help  quit

> (hbnb) 

> $

## Authors
- Hiba Elfaki [Github](https://github.com/hibakiz).
- Reem Hassanin [Github](https://github.com/reemelfadilhassanin).

## License

This project is a Public.
#### LAST UPDATE: 9 JAN 2024
