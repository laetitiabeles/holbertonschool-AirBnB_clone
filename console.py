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

    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return

        print(models.storage.all()[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
