#!/usr/bin/python3
"""Console module for HBNB project."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the program."""
        return True

    def do_quit(self, line):
        """Quit the program."""
        return True

    def help_quit(self):
        """Print help for quit command."""
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
