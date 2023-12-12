#!/usr/bin/python3
""" Console module for HBNB project"""

import cmd
import json
import datetime


class HBNBCommand(cmd.Cmd):
    """ a class that contains all the commands """
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing for empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        try:
            # Create an instance of the specified class
            from models.base_model import BaseModel
            obj = BaseModel()
            obj.save()

            # Print the newly created object's id
            print(obj.id)
        except ImportError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        from models import storage
        obj_dict = storage.all()
        key = args[0] + '.' + args[1]
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        from models import storage
        obj_dict = storage.all()
        key = args[0] + '.' + args[1]
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print string representations of all instances"""
        from models import storage
        obj_dict = storage.all()
        if not arg:
            print([str(obj_dict[key]) for key in obj_dict])
        elif arg == 'BaseModel':
            print([str(obj_dict[key]) for key in
                   obj_dict if key.split('.')[0] == 'BaseModel'])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        from models import storage
        obj_dict = storage.all()
        key = args[0] + '.' + args[1]
        if key not in obj_dict:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3].strip('"')

        # Skip updating if the attribute is 'id', 'created_at' or 'updated_at'
        if attr_name in ['id', 'created_at', 'updated_at']:
            return

        obj = obj_dict[key]
        setattr(obj, attr_name, attr_value)
        obj.updated_at = datetime.datetime.now()
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
