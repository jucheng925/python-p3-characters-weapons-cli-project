# lib/helpers.py
from models.character import Character
from models.weapon import Weapon


def blankline():
    print("")

def asterisk_line():
    print("****************************")

def display_all_characters():
    ## POSSIBLE NEED TO SWITCH TO FIND BY ID. AND NEED ERRORS
    characters = Character.get_all()
    display_all = True
    while display_all:
        blankline()
        print("Enter a Character's name for more details or hit 'ENTER' to return to the previous menu.")
        x = 1
        for character in characters:
            blankline()
            print(f'    {str(x)}', end= ". ")
            print(character)
            blankline()
            x +=1
        # print(f'    {x}. Press "Enter" to return to previous menu')
        name = input("> ")
        name = name.lower()
        if name == "":
            print("Returning to previous menu")
            display_all = False
        else:
            display_one_character(name)
    
def display_one_character(name):
    selected = Character.find_by_name(name)
    blankline()
    print(selected)
    print(selected.id)
    from cli import character_menu
    character_menu(selected)

def add_character():
    name = input("Enter the character's name: ")
    job_class = input("Enter the character's job class: ")
    name = name.lower()
    try:
        character = Character.create(name, job_class)
        print(f'Success in creating: {character}')
    except Exception as exc:
        print("Error creating character: ", exc)

def delete_character(character):
    try:
        delete_char = Character.find_by_id(character.id)
        delete_char.delete()
        print(f'{character} is deleted.')
    except Exception:
        print("Not successful in deleting character")




def exit_program():
    print("Goodbye!")
    exit()
