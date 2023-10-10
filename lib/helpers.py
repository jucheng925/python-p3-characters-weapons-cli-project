# lib/helpers.py
from models.character import Character
from models.weapon import Weapon

def blankline():
    print("")

def asterisk_line():
    print("****************************")

def display_all_characters():
    characters = Character.get_all()
    x = 1
    for character in characters:
        print(f'    {str(x)}', end= ". ")
        print(character)
        x +=1
    print("    Enter 'back' to return to previous menu")
    name = input("Please enter a character's name for more details: ")
    display_one_character(name)
    
def display_one_character(name):
    if name == "back":
        print("")
    else:
        selected = Character.find_by_name(name)
        print(selected)




def exit_program():
    print("Goodbye!")
    exit()
