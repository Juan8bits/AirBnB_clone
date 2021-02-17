# AirBnB_clone
This first part of the project aims to make a small-scale clone of AirBnB mostly corresponding to the backend.  It consists of building a command interpreter (console) that allows data management, from creating, updating, saving, displaying, among others, to users, places, descriptions, cities and different types of preset objects.

the following are the commands available in the console and a short description of how they function.
###Command table

| Command name | Description             | Use                                   |
| ------------------ | --------------------- |-----------------------------|
|`help`| Shows the commands available on the console or shows the guide for a specific command. | `help` or `help <command>`|
| `quit`        | Exit the program.                |  `exit`                                 |
| `create`    | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.                                     | `create <class name>`       |
| `show`      | Prints the string representation of an instance based on the class name and id.  |  `show <class name> <id>` |
|`destroy`  | Deletes an instance based on the class name and id (save the change into the JSON file). |  `destroy <class name> <id>` |
| `all`          | Prints all string representation of all instances based or not on the class name.  |   `all` or `all <class name>`|
|`update`    |Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).  | `update <class name> <id> <attribute name> "<attribute value>"` |

### **How to start and use it (with examples):**
**To start:**
- Clone this repo. `$ git clone https://github.com/Juan8bits/AirBnB_clone.git`
- Make sure you have python 3 installed in your VM or OS.
- Run file "Console.py" `$ ./console.py` or `$ python3 console.py`
- Now it´s ready to begin.  :D

**To use it:**
- Now, your prompt is '(hbnb)' and you can type the different commands are in the command table.
- for begging, you can use the command `create User` to create a first new object of type User.
- you should be see the id of the User created. as:

> (hbnb) create User
3ace6256-6756-4207-92a9-243ecac4d5ee
(hbnb)

- To see the created objects, you should use `all` or `show` command and get something like:

> (hbnb)show User 3ace6256-6756-4207-92a9-243ecac4d5ee
[User] (3ace6256-6756-4207-92a9-243ecac4d5ee) {'id': '3ace6256-6756-4207-92a9-243ecac4d5ee', 'updated_at': datetime.datetime(2021, 2, 17, 19, 22, 52, 127143), 'created_at': datetime.datetime(2021, 2, 17, 19, 22, 52, 127143)}
(hbnb)

- With  `all User` with xx will see all objects of type User in a list but in this case, only have one created.

> (hbnb)all User
["[User] (3ace6256-6756-4207-92a9-243ecac4d5ee) {'id': '3ace6256-6756-4207-92a9-243ecac4d5ee', 'updated_at': datetime.datetime(2021, 2, 17, 19, 22, 52, 127143), 'created_at': datetime.datetime(2021, 2, 17, 19, 22, 52, 127143)}"]
(hbnb)

- In the directory, the file "file.json" should be have the directory of all objects in JSON style.
- In the same way, you can implement the different commands to delete and update (You can add new attributes to the different objects).

### Learning Objectives
- How to create a Python package.
- How to create a command interpreter in Python using the `cmd` module.
- What is Unit testing and how to implement it in a large project.
- How to serialize and deserialize a Class.
- How to write and read a JSON file.
- How to manage `datetime`.
- What is an` UUID`.
- What is `*args` and how to use it.
- What is `**kwargs` and how to use it.
- How to handle named arguments in a function.

---
### Resources
- [cmd module](https://docs.python.org/3.4/library/cmd.html)
- [packages concept page](https://docs.python.org/3.4/tutorial/modules.html#packages)
- [uuid module](https://docs.python.org/3.4/library/uuid.html)
- [datetime](https://docs.python.org/3.4/library/datetime.html)
- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [args/kwargs](https://realpython.com/python-kwargs-and-args/)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
---
### **Author**
**Juan Manuel Ramirez Saa** - [*Juan8bits*](https://github.com/Juan8bits)

