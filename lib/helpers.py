# lib/helpers.py
from models.character import Character
from models.weapon import Weapon
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
import random

custom_theme = Theme({"success":"green" , "error": "bold red"})
console = Console(theme = custom_theme)

def blankline():
    print("")

def asterisk_line():
    console.print("****************************", style ="bold")

def display_job_classes():
    str_format = ', '.join(Character.JOBCLASS)
    console.print("    Selectable job Class:                        ", style ="bold cyan on grey42")
    console.print(f'    {str_format}', style ="italic bold on grey42")

def display_all_characters():
    table = Table(title ="All Characters", show_lines ="True", width=42)
    table.add_column("Name", style="bold slate_blue3", justify="center", ratio=3)
    table.add_column("Job Class", style="bold cyan", justify="center",ratio =3)
    table.add_column("Money", style="italic turquoise4", ratio=2)
    characters = Character.get_all()
    for character in characters:
        table.add_row(character.name, character.job_class, f'${character.money}')
    console.print(table)

def validate_selection(choice):
    selected_character = Character.find_by_name(choice.title())
    from cli import character_menu
    character_menu(selected_character) if selected_character else console.print(f'Character {choice} not found.', style ="error")


def add_character():
    name = input("Enter the character's name: ")
    display_job_classes()
    job_class = input("Enter the character's job class: ")
    money = input('Enter a starting money amount or press "Enter" for the default amount: ')
    try:
        if money == "": money = "100"
        character = Character.create(name, job_class.title(), int(money))
        console.print(f'Success in creating: {character}', style ="success")
    except Exception as exc:
        console.print("Error creating character: ", exc, style ="error")

def delete_character(delete_char):
    weapons = delete_char.weapons()
    if weapons: [weapon.delete() for weapon in weapons]
    delete_char.delete()
    console.print(f'{delete_char} is deleted.', style ="success")


def update_character(character):
    try:
        name = input(f'Enter a new name for {character.name} or press "Enter" to keep it the same: ')
        if name != "": character.name = name
        display_job_classes()
        job_class = input('Enter the character\'s new job class or press "Enter" to keep it the same: ')
        if job_class != "": character.job_class = job_class.title()
        input('Can not change money amount, press "Enter" to acknowledge: ')
        character.update()
        blankline()
        console.print(f'Success in updating: {character}', style ="success")
        blankline()
    except Exception as exc:
        console.print("Error in updating character: ", exc, style ="error")

def display_weapons(char):
    weapons = char.weapons()
    if weapons:
        console.print(f'{char.name} has ${char.money}.', style="bold")
        table = Table(title=f"{char.name}'s Weapon(s)", show_lines="true")
        table.add_column("Weapon Type")
        table.add_column("Damage Value")
        table.add_column("Cost Value")
        for weapon in weapons:
            table.add_row(weapon.type, str(weapon.damage_value), f'${weapon.cost_value}')
        console.print(table)
    else:
        console.print(f'{char.name} has ${char.money} and does not have any weapons.', style="error")

def add_weapon(char):
    blankline()
    weapon_type = input("Enter the type of weapon: ")
    damage_value = int(input("Enter the weapon's damage value (from 0 to 10): "))
    input('The price of the weapon will be randomly generate. Press "Enter" to acknowledge: ')
    blankline()
    try:
        cost_value = random.randrange(10,51)
        weapon = Weapon.create(weapon_type, damage_value, cost_value, char.id)
        console.print(f'Success in creating: {weapon}', style="success")
        char.adjust_money(-cost_value)
        print(f'**Money spent: ${cost_value}')
        blankline()
    except Exception as exc:
        console.print("Error creating weapon: ", exc, style ="error")
        console.print("Not successful in buying weapon, please try again!", style ="error")
        blankline()

def delete_weapon(char):
    weapon_type = input("Enter the weapon type that you want to sell: ")
    try:
        weapon_to_delete = Weapon.find_by_type(weapon_type.upper())
        price = weapon_to_delete.cost_value
        char.adjust_money(price)
        weapon_to_delete.delete()
        console.print(f'{weapon_type} was sold for ${price}', style ="success")
        blankline()
    except Exception:
        console.print("Not successful in selling weapon. Please try again.", style ="error")
        blankline()

def display_all_weapons():
    table = Table(title="All Available Weapons", show_lines="true")
    table.add_column("Weapon Type")
    table.add_column("Damage Value")
    table.add_column("Cost Value")
    table.add_column("Owner Name")
    weapons = Weapon.get_all()
    for weapon in weapons:
        table.add_row(weapon.type, str(weapon.damage_value), f'${weapon.cost_value}', weapon.owner_name())
    console.print(table)    

def trade_partner(char, trade_part):
    if trade_part.title() == char.name:
        console.print("Can not trade with your character. Please select another character.", style ="error") 
    else:
        trade_character = Character.find_by_name(trade_part.title())
        if trade_character:
           trade(char, trade_character)
        else:
            console.print("Error finding the character, please try again", sytle ="error")

def trade(my_char, trade_char):
    while True:
        trade_char_weapon = choose_weapon(trade_char)
        my_weapon = choose_weapon(my_char)
        if trade_char_weapon and my_weapon:
            confirm_trade(trade_char, trade_char_weapon, my_char, my_weapon)
        else:
            console.print("Trade not successful. Please try again.", style ="error")

def choose_weapon(char):
    display_weapons(char)
    trade_weapon = input(f"Choose one of {char.name}\'s weapon that will be trade: ")
    trade_weapon = Weapon.find_by_type(trade_weapon.upper())
    return trade_weapon if trade_weapon else console.print("Weapon not found, please check spelling.", style ="error")


def confirm_trade(trade_char, trade_character_weapon, my_char, my_weapon):
    asterisk_line()
    print(f"The trade will be between {trade_char.name} and {my_char.name}")
    print(f'    {trade_character_weapon.type} will be exchange for {my_weapon.type}')
    confirm = input("Press 'Y' or 'y' to confirm the trade or press any other keys to cancel: ")
    if confirm == ("y" or "Y"):
        my_weapon.owner_id = trade_char.id
        trade_character_weapon.owner_id = my_char.id
        my_weapon.update()
        trade_character_weapon.update()
        console.print("Trade completed", style ="success")
        from cli import character_menu
        character_menu(my_char)
    else:
        console.print("Trade did not occur.", style ="error")
        console.print("Returning to previous menu", style ="error")
        from cli import trade_menu
        trade_menu(my_char)


def exit_program():
    print("Goodbye!")
    exit()
