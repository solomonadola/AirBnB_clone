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
import re


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

    def do_update(self, arg):
        """Update an instance based on the class name and id with a dictionary"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** dictionary missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            all_objects = storage.all()
            key = class_name + "." + instance_id

            if key not in all_objects:
                print("** no instance found **")
            else:
                obj = all_objects[key]
                # Convert the dictionary representation to a dictionary
                try:
                    update_dict = eval(args[2])
                except Exception as e:
                    print("** invalid dictionary format **")
                    return

                if not isinstance(update_dict, dict):
                    print("** invalid dictionary format **")
                else:
                    for key, value in update_dict.items():
                        # Update the attributes of the object
                        setattr(obj, key, value)
                    obj.save()


    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
