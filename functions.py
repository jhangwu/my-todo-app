# functions code for experiment10

def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of to_do items."""
    with open(filepath, "r") as content:
        todos_local = content.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello There!")
    print(get_todos())
