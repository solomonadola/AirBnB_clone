#!/usr/bin/python3
""" Console module for HBNB project"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNB command calss"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing for empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
