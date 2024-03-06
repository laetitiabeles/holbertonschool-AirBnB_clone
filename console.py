#!/usr/bin/python3
""" Console module """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Handle console monitor class
    Args:
        cmd: cmd class inheritance
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print('')
        return True

    def emptyline(self):
        """Empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
