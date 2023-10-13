# lib/helpers.py
from models.character import Character
from models.weapon import Weapon


def blankline():
    print("")

def asterisk_line():
    print("****************************")

def display_all_characters():
    characters = Character.get_all()
    while True:
        blankline()
        print("Enter a selection for more details: ")
        x = 1
        for character in characters:
            character.position = x
            print(f'    {character.position}', end= ". ")
            print(character)
            blankline()
            x +=1
        print(f'    {x}. or press "Enter" to return to previous menu.')
        try: 
            choice = input("> ")
            if choice == "" or choice == str(x):
                print("Returning to previous menu")
                break
            elif int(choice) in range(1, x):
                char = [character for character in characters if character.position == int(choice)]
                from cli import character_menu
                character_menu(char[0])
            else:
                print("Invalid number - need to be one of the listed number.")
        except ValueError:
            print("Invalid selection - selection must be a number")


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
        weapons = delete_char.weapons()
        [weapon.delete() for weapon in weapons]
        delete_char.delete()
        print(f'{character} is deleted.')
    except Exception:
        print("Not successful in deleting character")




def exit_program():
    print("Goodbye!")
    exit()
