# CLI+ORM Project: Game World
*A menu-based project for game characters and their weapons*

## Description 
This is a CLI **(Command Line Interface)** and ORM **(Object Relational Mapping)**project that is written in Python. Each instance created/updated will be save in a SQLlite database in the background through Python ORM methods. This project will have 2 model classes (Character and Weapon) with a one-to-many relationships between them. 

---
### To get started:
First, run the below code to install the dependencies and set up the virtual environment:
```
pipenv install
pipenv shell
```

Next, we need to create and set up the table for the SQL database. If you want to start with an empty table run:
```
python lib/reset.py
```
Note: you can use this code when you want to clear the database and restart with an empty table.

However, instead if you prefer to have some data already created and pre-populated on the database to work with run:
```
python lib/seed.py
```

Once both the environment and the database is set up, run the following code to start the program.
```
python lib/cli.py
```

### File Directory Structure

```
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── character.py   
    │   └── weapon.py
    ├── cli.py
    ├── helpers.py
    ├── reset.py
    └── seed.py
```

### Files
Cli.py is the main file where the main execusion of the program takes place. This is where all the menus (main and submenus) are written and contain the logic in determing which helper function should be run next depending on the user's input.

In the helpers.py file, all the helpers functions are written and defined. These functions act as an intermediate and will display the data from the database (which the user does not see). These functions could range from something simple like updating the character's name to something more complex like changing the owner of a weapon through a trade.

As mentioned before, the reset.py file once execute will create empty database tables without any data while the seed.py file will create database tables with pre-populated data.

In the models file, there are two files (Character and Weapon). Each file describe its respectivelly named class, instance attributes, and both instance methods and class methods. All of the ORM methods are defined in the class definition.

---

## Menus
Below is a brief overlook of the menus/submenus in this project

Main menu:
1. Display all characters
2. Add a new character
3. Exit

Individual Character Menu:
Brief Summary - of the selected character (character name, job class, weapons) 
1. Update character name or job_class
2. Delete selected character (including all the weapons it has)
2. Display all of the character's weapons
3. Return to previous menu

Weapon Menu:
Brief Summary of all the weapon belonging to the selected character
1. Buy a custom made weapon (*add*)
2. Sell one of the weapon (*delete*)
3. Trade weapon with another character
4. Return to previous menu

Trade menu:
*Note: Instead of a numbered menu, this menu will ask for an user input with one question at a time. There will be input validation going on at the same time.*
All weapons will be displayed with their corresponding owners.
The first input needed from the user would be the trade partner/character they want to trade with. The next input would be the weapon that they are intersted in getting. Then they will have to select the weapon from their inventory to trade with. Once both weapons are selected, there will be a confirmation message to confirm the trade.

## Format
This project use the Rich for formating, as seem by the color fonts and table display. [Rich docs](https://rich.readthedocs.io/en/stable/index.html)

## Conclusion
Even though this project produces a simple CLI application, a lot of background functions happen in the background. This has been a good experience for me especially with managing all these moving parts. I hope you enjoy what I have created.
