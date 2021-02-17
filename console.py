#!/usr/bin/python3
""" Module program called console.py that contains
    the entry point of the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from shlex import split


class HBNBCommand(cmd.Cmd):
    """Information about this shit """
    prompt = "(hbnb)"
    __Models = ["BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Place",
                "Review"
                ]

    def do_create(self, args):
        """->Use: (hbnb)create <class name>

        Method that Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        list_arg = split(args)
        if len(list_arg) == 0:
            print("** class name missing **")
        elif len(list_arg) == 1:
            if list_arg[0] not in self.__Models:
                print("** class doesn't exist **")
            else:
                new_instance = eval(list_arg[0])()
                print(new_instance.id)
                storage.save()

    def do_show(self, args):
        """->Use: show <class name> <id>

        Method to prints the string representation of an
        instance based on the class name and id.
        """
        list_arg = split(args)
        if len(list_arg) == 0:
            print("** class name missing **")
        else:
            if list_arg[0] not in self.__Models:
                print("** class doesn't exist **")
            elif len(list_arg) == 1:
                print("** instance id missing **")
            else:
                obj = list_arg[0] + "." + list_arg[1]
                if obj not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[obj])

    def do_destroy(self, args):
        """->Use: (hbnb)destroy <class name> <id>

        Method that deletes an instance based on the class
        name and id (save the change into the JSON file).
        """
        list_arg = split(args)
        if len(list_arg) == 0:
            print("** class name missing **")
        else:
            if list_arg[0] not in self.__Models:
                print("** class doesn't exist **")
            elif len(list_arg) == 1:
                print("** instance id missing **")
            else:
                obj = list_arg[0] + "." + list_arg[1]
                if obj not in storage.all().keys():
                    print("** no instance found **")
                else:
                    storage.all().pop(obj)
                    storage.save()

    def do_all(self, args):
        """->Use:(hbnb)all or: (hbnb)all <class name>

        Method that prints all string representation of all
        instances based or not on the class name.
        """
        list_ar = split(args)
        if len(list_ar) == 0:
            l = [str(v) for v in storage.all().values()]
            print(l)
        elif len(list_ar) > 0 and list_ar[0] not in self.__Models:
            print("** class doesn't exist **")
        else:
            cls_ = list_ar[0]
            dic_ob = storage.all().values()
            l = [str(v) for v in dic_ob if v.__class__.__name__ == cls_]
            print(l)

    def do_update(self, args):
        """->Use:(hbnb)update <class name> <id> <attribute name> "<attribute value>"

        Method Updates an instance based on the class name and
        id by adding or updating attribute (save the change into
        the JSON file).

        Terms:
        Only one attribute can be updated at the time
        """
        list_arg = split(args)
        print(str(list_arg))
        if len(list_arg) == 0:
            print("** class name missing **")
        elif list_arg[0] not in self.__Models:
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        else:
            obj = list_arg[0] + "." + list_arg[1]
            if obj not in storage.all().keys():
                print("** no instance found **")
            elif len(list_arg) == 2:
                print("** attribute name missing **")
            elif len(list_arg) == 3:
                print("** value missing **")
            else:
                dic_ob = storage.all()[obj]
                """#if list_arg[3].isdigit():
                #    list_arg[3] = int(list_arg[3])
                #else:
                #    try:
                #        list_arg[3] = float(list_arg[3])
                #    except ValueError:
                #        pass
                """
                attributte = list_arg[2]
                value = list_arg[3]
                setattr(dic_ob, attributte, value)
                storage.save()

    def do_EOF(self, args):
        """End of file interruption.
        """
        return True

    def do_quit(self, args):
        """->Use: (hbnb)quit

        Use this command when you need to exit/close the program.
        """
        return True

    def emptyline(self):
        """Clean command given"""
        pass

if __name__ == '__main__':
    shell = HBNBCommand()
    shell.cmdloop()
