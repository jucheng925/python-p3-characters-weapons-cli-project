# CLI+ORM Project: Game World
*A menu-based project for game characters and their weapons*

## Description 
This is a CLI **(Command Line Interface)** and ORM **(Object Relational Mapping)**project that is written in Python. Each instance create/update will be save in a SQL lite database in the background through Python ORM methods. This project will have 2 model classes (Character and Weapon) with a one-to-many relationships between them. 

---------
### To get started:
First, run the below code to install the dependencies and set up the virtual environment:
```
pipenv install
pipenv shell
```

Next, we need to create and set up the table for the SQL database. If you want to start with an empty table run:
`python lib/reset.py` 
Note: you can use this code when you want to clear the database and restart with an empty table.

However, instead if you prefer to have some data already created and pre-populated on the database to work with run:
`python lib/seed.py`

Once both the environment and the database is set up, run the following code to start the program.
`python lib/cli.py`

### File Structure
```
lib
|-- cli.py
|-- debug.py
|-- helpers.py
|-- reset.py
|-- seed.py
|__ models
    |-- __init__.py
    |-- character.py
    |-- weapon.py

```

###
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

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)


MENU 
Main menu:
    Welcome to Fantasy Land =>done
       **Choose a character**
    1. Display All Characters
    2. Add a custom character
    4. Exit
** note - should have a list of jobclass! (need to work on)

Display All Characters menu ==>done
    1. Bob
    2. sam
    3. Anna
    etc
    4. Go back to previous menu

Display individual character
    print out character name, job_class, weapons 
    1. update character name or job_class --> done
    2. delete selected character (including all the weapons it has)  ==> done
    2. Display all weapons for that character
    3. return to previous menu

display character's weapon
    print all weapons belonging to the characters
    1. want to trade a weapon?
    2. or just want to sell of your weapon(delete) --done
    3. add a custom made weapon? -->done
    4. return to previous menu


trade menu:
    Who do you want to trade with?
    **display all weapons including your own, but make sure you can not select your own** - to make minimal requirement - of display all
    once a character selected - show their weapons
    let user choose a weapon
    then ask use to select a weapon they have.
    ask: "Please confirm the trade(Y/N)"
    return to previous menu


