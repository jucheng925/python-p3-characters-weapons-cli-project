# Phase 3 CLI+ORM Project Template

ORM Requirements
The application must include a database created and modified with Python ORM methods that you write.

The data model must include at least 2 model classes.
The data model must include at least 1 one-to-many relationships.
Property methods should be defined to add appropriate constraints to each model class.
Each model class should include ORM methods (create, delete, get all, and find by id at minimum).
CLI Requirements
The CLI must display menus with which a user may interact.
The CLI should use loops as needed to keep the user in the application until they choose to exit.
For EACH class in the data model, the CLI must include options: to create an object, delete an object, display all objects, view related objects, and find an object by attribute.
The CLI should validate user input and object creations/deletions, providing informative errors to the user.
The project code should follow OOP best practices.
Pipfile contains all needed dependencies and no unneeded dependencies.
Imports are used in files only where necessary.
Project folders, files, and modules should be organized and follow appropriate naming conventions.
The project should include a README.md that describes the application.
You do not need to implement tests for pytest, although you should test your code thoroughly using your CLI. Try entering bad data when prompted for input, and confirm your application prints a useful error message## Requirements


## Learning Goals

- Discuss the basic directory structure of a CLI.
- Outline the first steps in building a CLI.

---

## Introduction

You now have a basic idea of what constitutes a CLI. Fork and clone this lesson
for a project template for your CLI.

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── model_1.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

Note: The directory also includes two files named `CONTRIBUTING.md` and
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard or
delete the files if you want.

---

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```

You can run the template CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. The template CLI will ask for input, do
some work, and accomplish some sort of task.

Past that, CLIs can be whatever you'd like, as long as you follow the project
requirements.

Of course, you will update `lib/cli.py` with prompts that are appropriate for
your application, and you will update `lib/helpers.py` to replace `helper_1()`
with a useful function based on the specific problem domain you decide to
implement, along with adding other helper functions to the module.

In the `lib/models` folder, you should rename `model_1.py` with the name of a
data model class from your specific problem domain, and add other classes to the
folder as needed. The file `lib/models/__init__.py` has been initialized to
create the necessary database constants. You need to add import statements to
the various data model classes in order to use the database constants.

You are also welcome to implement a different module and directory structure.
However, your project should be well organized, modular, and follow the design
principal of separation of concerns, which means you should separate code
related to:

- User interface
- Data persistence
- Problem domain rules and logic

---

## Updating README.md

`README.md` is a Markdown file that should describe your project. You will
replace the contents of this `README.md` file with a description of **your**
actual project.

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this assignments's resources for a basic guide to Markdown.

### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)





MENU 
Main menu:
    Welcome to Fantasy Land
       **Choose a character**
    1. Display All Characters
    2. Add a custom character
    3. delete character
    4. Exit

Display All Characters menu
    1. Bob
    2. sam
    3. Anna
    etc
    4. Go back to previous menu

Display individual character
    print out character name, job_class, weapons
    1. update character name or job_class
    2. Display all weapons for that character
    3. return to previous menu

display character's weapon
    print all weapons belonging to the characters
    1. want to trade a weapon?
    2. or just want to sell of your weapon(delete)
    3. add a custom made weapon?
    4. return to previous menu


trade menu:
    Who do you want to trade with?
    **display all other characters except for you**
    once a character selected - show their weapons
    let user choose a weapon
    then ask use to select a weapon they have.
    ask: "Please confirm the trade(Y/N)"
    return to previous menu


