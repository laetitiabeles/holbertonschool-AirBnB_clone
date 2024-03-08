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
        """Create command to create a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        instance = getattr(models, class_name)()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Show command to show an instance """
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        all_objects = models.storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in all_objects:
            print("** no instance found **")
            return

        print(all_objects[key])

    def do_destroy(self, line):
        """ Destroy an instance """
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        all_objects = models.storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in all_objects:
            print("** no instance found **")
            return

        del all_objects[key]
        models.storage.save()

    def do_all(self, line):
        """Print all instances from the storage"""
        all_objects = models.storage.all()

        if not line:
            print([str(instance) for instance in all_objects.values()])
        else:
            args = shlex.split(line)
            class_name = args[0]

            if class_name not in models.classes:
                print("** class doesn't exist **")
                return

            for instance in all_objects.values():
                if type(instance).__name__ == class_name:
                    print(str(instance))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
