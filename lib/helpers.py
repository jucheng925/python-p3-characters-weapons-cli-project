# lib/helpers.py
from models.character import Character
from models.weapon import Weapon
import random


def blankline():
    print("")

def asterisk_line():
    print("****************************")

def display_all_characters():
    characters = Character.get_all()
    while True:
        asterisk_line()
        print("Enter a selection for more details: ")
        x = 1
        for character in characters:
            character.position = x
            print(f'    {character.position}', end= ". ")
            print(character)
            blankline()
            x +=1
        print(f'    {x}. Or press "Enter" to return to previous menu.')
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
    money = input('Enter a starting money amount or press "Enter" for the default amount: ')
    name = name.lower()
    try:
        if money == "": money = "100"
        character = Character.create(name, job_class, int(money))
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

def update_character(character):
    update_char = Character.find_by_id(character.id)
    try:
        name = input(f'Enter a new name for {character.name} or press "Enter": ')
        if name != "": update_char.name = name
        job_class = input('Enter the character\'s new job class: ')
        if job_class != "": update_char.job_class = job_class
        message = input('Can not change money amount, press "Enter" to acknowledge: ')
        print(message)

        update_char.update()
        print(f'Success in updating: {update_char}')
        blankline()
    except Exception as exc:
        print("Error in updating character: ", exc)

def display_weapons(char):
    weapons = char.weapons()
    if weapons:
        print(f"The weapon(s) that belongs to {char.name}: ")
        for weapon in weapons:
            blankline()
            print(f'    -- {weapon}')
        blankline()
    else:
        print(f'{char.name} does not have any weapons.')

def add_weapon(char):
    blankline()
    weapon_type = input("Enter the type of weapon: ")
    damage_value = int(input("Enter the weapon's damage value (from 0 to 10): "))
    message = input('The price of the weapon will be randomly generate. Press "Enter" to acknowledge: ')
    blankline()
    if message == "": 
        try:
            cost_value = random.randrange(10,51)
            weapon = Weapon.create(weapon_type, damage_value, cost_value, char.id)
            print(f'Success in creating: {weapon}')
            char.spend(cost_value)
            print(f'**Money spent: ${cost_value}')
            blankline()
        except Exception as exc:
            print("Error creating weapon: ", exc)
            print("Not successful in buying weapon, please try again!")
            blankline()
    else: 
        print("Not successful in buying weapon, please try again!")
        blankline()

def delete_weapon(char):
    weapon_type = input("Enter the weapon type to sell: ")
    try:
        weapon_to_delete = Weapon.find_by_type(weapon_type.upper())
        price = weapon_to_delete.cost_value
        char.sell(price)
        weapon_to_delete.delete()
        print(f'{weapon_type} was sold for ${price}')
        blankline()
    except Exception:
        print("Not successful in deleting weapon")
        blankline()




def exit_program():
    print("Goodbye!")
    exit()
