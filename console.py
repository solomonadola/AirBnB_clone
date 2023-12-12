#!/usr/bin/python3
"""Console module for AirBnB"""

import cmd
import sys
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "
    classes = ["BaseModel", "City", "State", "Review", "Amenity", "Place"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF"""
        print("")  # Print a newline for better formatting
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_destroy(self, arg):
        """Destroy an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objects = storage.all()
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        args = arg.split()
        all_objects = storage.all()

        if not args:
            print([str(all_objects[obj]) for obj in all_objects])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instances = [str(all_objects[obj]) for obj in all_objects
                         if class_name in obj]
            print(instances)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            all_objects = storage.all()
            if key in all_objects:
                obj = all_objects[key]
                setattr(obj, args[2], args[3].strip('"'))
                obj.save()
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """Count the number of instances of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instances_count = sum(1 for obj in storage.all().values()
                                  if class_name == obj.__class__.__name__)
            print(instances_count)

    def do_show(self, arg):
        """Show the string representation of an instance by ID"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objects = storage.all()
            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

    def default(self, line):
        """Handle custom commands"""
        parts = line.split('.')
        if len(parts) == 2:
            class_name = parts[0]
            command = parts[1].split('(')[0]
            if command == 'count()':
                instances_count = sum(1 for obj in storage.all().values()
                                      if class_name == obj.__class__.__name__)
                print(instances_count)
            elif command == 'all()':
                instances = [str(obj) for obj in storage.all().values()
                             if class_name == obj.__class__.__name__]
                print(instances)
            elif command == 'show':
                # Extract ID from the command
                id_str = parts[1].split('(')[1].strip(')').strip('"')
                key = class_name + "." + id_str
                all_objects = storage.all()
                if key in all_objects:
                    print(all_objects[key])
                else:
                    print("** no instance found **")
            else:
                super().default(line)
        else:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
