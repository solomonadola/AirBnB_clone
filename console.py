#!/usr/bin/python3
"""
Console module
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.
        """
        if not line:
            print("** class name missing **")
            return
        try:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            print(storage.all().get(key, "** no instance found **"))
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all()
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        args = line.split()
        instances = storage.all()
        if not args or args[0] not in storage.classes():
            print([str(obj) for obj in instances.values()])
        else:
            try:
                class_name = args[0]
                print([str(obj) for key, obj in instances.items()
                       if class_name in key])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
                return

            instance = instances[key]
            if len(args) < 3:
                print("** attribute name missing **")
                return

            attr_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return

            attr_value_str = args[3]
            attr_value = None

            if '"' in attr_value_str:
                attr_value = attr_value_str.strip('"')
            else:
                try:
                    attr_value = int(attr_value_str)
                except ValueError:
                    try:
                        attr_value = float(attr_value_str)
                    except ValueError:
                        pass

            if attr_value is None:
                print("** value missing **")
                return

            setattr(instance, attr_name, attr_value)
            instance.save()

        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
        except AttributeError:
            print("** attribute name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
