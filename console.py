#!/usr/bin/python3
""" Console module """

import cmd
import shlex
import models


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

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        return

        args = shlex.split(line)
        class_name = args[0]

        if line not in models.classes:
            print("** class doesn't exist **")
            return

        instance = getattr(models, class_name)()
        instance.save()
        print(instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
