# lib/helpers.py
from models.character import Character
from models.weapon import Weapon
from prettytable import PrettyTable
import random


def blankline():
    print("")

def asterisk_line():
    print("****************************")

def job_class_table():
    table = PrettyTable()
    job_list = Character.JOBCLASS
    table.add_row([job_list[0], job_list[1]])

def display_all_characters():
    char_table = PrettyTable()
    char_table.field_names = ["Name", "Job Class", "Money"]
    characters = Character.get_all()
    for character in characters:
        char_table.add_row([character.name, character.job_class, character.money], divider = True)
    print(char_table)

def validate_selection(choice):
    selected_character = Character.find_by_name(choice.title())
    from cli import character_menu
    character_menu(selected_character) if selected_character else print(f'Character {choice} not found.')


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
    try:
        name = input(f'Enter a new name for {character.name} or press "Enter" to keep it the same: ')
        if name != "": character.name = name
        print(Character.JOBCLASS)
        job_class = input('Enter the character\'s new job class or press "Enter" to keep it the same: ')
        if job_class != "": character.job_class = job_class
        message = input('Can not change money amount, press "Enter" to acknowledge: ')
        print(message)

        character.update()
        print(f'Success in updating: {character}')
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

def display_all_weapons():
    table = PrettyTable()
    table.field_names = ["Weapon Type", "Damage Value", "Cost Value", "Owner Name"]
    weapons = Weapon.get_all()
    for weapon in weapons:
        table.add_row([weapon.type, weapon.damage_value, weapon.cost_value, weapon.owner_name()])
    table.align = "l"
    print(table)    

def trade_partner(char, trade_name):
    if trade_name.title() == char.name:
        print("Can not trade with your selected character. Please select another character.")
    else:
        trade_character = Character.find_by_name(trade_name.title())
        if trade_character:
           trade(trade_character, char)

        else:
            print("Error finding the character, please try again")

def trade(trade_char, selected_char):
    display_weapons(trade_char)
    trade_character_weapon = input(f'Choose one of the weapon from {trade_char.name}: ')
    if not Weapon.find_by_type(trade_character_weapon.upper()):
        print("Weapon not found, please try again")
        trade(trade_char, selected_char)
            
    display_weapons(selected_char)
    trade_weapon = input(f"Choose one of {selected_char.name}\'s weapon that will be exchange for {trade_character_weapon}: ")
    if not Weapon.find_by_type(trade_weapon.upper()):
        print("Weapon not found, please try again")
        trade(trade_char, selected_char)

    confirm_trade(trade_char, trade_character_weapon, selected_char, trade_weapon)

def confirm_trade(trade_char, trade_character_weapon, selected_char, trade_weapon):
    asterisk_line()
    print(f"The trade will be between {trade_char.name} and {selected_char.name}")
    print(f'    {trade_character_weapon.upper()} will be exchange for {trade_weapon.upper()}')
    confirm = input("Press 'y' to confirm the trade or press any other keys to cancel: ")
    if confirm == ("y" or "Y"):
        trade_weapon_1 = Weapon.find_by_type(trade_character_weapon.upper())
        trade_weapon_1.owner_id = selected_char.id 
        trade_weapon_2 = Weapon.find_by_type(trade_weapon.upper())
        trade_weapon_2.owner_id = trade_char.id
        trade_weapon_1.update()
        trade_weapon_2.update()
        print("Trade completed")
    else:
        print("Trade did not occur.")
        print("Returning to previous menu")

def exit_program():
    print("Goodbye!")
    exit()
