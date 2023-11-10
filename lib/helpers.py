# lib/helpers.py
from models.character import Character
from models.weapon import Weapon
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
import random
import copy

custom_theme = Theme({"success":"bold green" , "error": "bold red", "name": "bold cyan", "money": "italic turquoise4", "jobclass":"bold magenta"})
console = Console(theme = custom_theme)

def blankline():
    print("")

def asterisk_line():
    console.print("****************************", style ="bold")

def display_job_classes():
    str_format = ', '.join(Character.JOBCLASS)
    console.print("    Selectable job Class:                          ", style ="bold cyan on khaki1")
    console.print(f'    {str_format} ', style ="italic bold magenta on khaki1")

def display_all_characters():
    table = Table(title ="ALL CHARACTERS", show_lines ="True", width=42)
    table.add_column("Name", style="name", ratio=3)
    table.add_column("Job Class", style="jobclass", ratio =3)
    table.add_column("Money", style="money", ratio=2)
    characters = Character.get_all()
    for character in characters:
        table.add_row(character.name, character.job_class, f'${character.money}')
    console.print(table)

def validate_selection(choice):
    selected_character = Character.find_by_name(choice.title())
    from cli import character_menu
    character_menu(selected_character) if selected_character else console.print(f'Character [name]{choice.title()}[/] not found.', style ="error")


def add_character():
    console.print("Enter the character's name", style="bold", end="")
    name = input(": ")
    display_job_classes()
    console.print("Enter the character's job class", style="bold", end="")
    job_class = input(": ")
    console.print('Enter a starting money amount or press "Enter" for the default amount:', style ="bold", end="")
    money = input(": ")
    try:
        if money == "": money = "100"
        character = Character.create(name, job_class.title(), int(money))
        console.print(f'[success]Success in creating: {character}[/]')
    except Exception as exc:
        console.print("Error creating character: ", exc, style ="error")

def delete_character(delete_char):
    weapons = delete_char.weapons()
    if weapons: [weapon.delete() for weapon in weapons]
    delete_char.delete()
    console.print(f'{delete_char} is deleted.', style ="success")


def update_character(character):
    original_char = copy.deepcopy(character)            
    try:
        console.print(f'Enter a new name for [name]{character.name}[/] or press "Enter" to keep it the same', style="bold", end="")
        name = input(": ")
        if name != "": character.name = name
        display_job_classes()
        console.print('Enter the character\'s new job class or press "Enter" to keep it the same', style="bold", end="")
        job_class = input(": ")
        if job_class != "": character.job_class = job_class.title()
        console.print('Can not change money amount, press "Enter" to acknowledge', style ="bold dark_red", end="")
        input(": ")
        character.update()
        blankline()
        console.print(f'[success]Success in updating: {character}[/]')
        blankline()
    except Exception as exc:
        console.print("Error in updating character: ", exc, style ="error")
        character.name = original_char.name
        


def display_weapons(char):
    weapons = char.weapons()
    if weapons:
        console.print(f'[name]{char.name}[/] has [money]${char.money}[/].')
        table = Table(title=f"{char.name}'s Weapon(s)", show_lines="true", width=42)
        table.add_column("Weapon Type", style="bold", ratio=4)
        table.add_column("Damage Value", style="hot_pink3", ratio=2)
        table.add_column("Cost Value", style="money",ratio=2)
        for weapon in weapons:
            table.add_row(weapon.type, str(weapon.damage_value), f'${weapon.cost_value}')
        console.print(table)
    else:
        console.print(f'[name]{char.name}[/] has [money]${char.money}[/] and does not have any weapons.', style="bold dark_red")

def add_weapon(char):
    blankline()
    console.print("Enter the [bold]WEAPON TYPE[/]", end="")
    weapon_type = input(": ")
    console.print("Enter the weapon's damage value ([hot_pink3]from 0 to 10[/])", end="")
    damage_value = input(": ")
    console.print('The price of the weapon will be randomly generate. Press "Enter" to acknowledge', style="bold dark_red", end="")
    input(': ')
    blankline()
    try:
        cost_value = random.randrange(10,51)
        if char.money > cost_value:
            char.adjust_money(-cost_value)
            weapon = Weapon.create(weapon_type, int(damage_value), cost_value, char.id)
            console.print(f'**Money spent: [money]${cost_value}[/].**', style="success")
            console.print(f'[success]Success in creating: {weapon}[/]')
        else:
            console.print("Do not have enough money to buy!", style="error")
    except Exception as exc:
        console.print("Not successful in buying weapon, please try again!", exc, style ="error")


def delete_weapon(char):
    console.print("Enter the [bold]WEAPON TYPE[/] that you want to sell")
    weapon_type = input(": ")
    try:
        weapon_to_delete = Weapon.find_by_type(weapon_type.upper())
        price = weapon_to_delete.cost_value
        char.adjust_money(price)
        weapon_to_delete.delete()
        console.print(f'{weapon_type.upper()} was sold for [money]${price}[/].', style ="success")
        blankline()
    except Exception:
        console.print("Not successful in selling weapon. Please try again.", style ="error")
        blankline()

def display_all_weapons():
    table = Table(title="ALL AVAILABLE WEAPONS", show_lines="true", width=55)
    table.add_column("Weapon Type", ratio=3, style ="bold")
    table.add_column("Damage Value", ratio=2, style="hot_pink3")
    table.add_column("Cost Value", ratio=2, style="money")
    table.add_column("Owner Name", ratio=2, style ="name")
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
            console.print("Error finding the character, please try again", style ="error")

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
    console.print(f"From [name]{char.name}\'s[/] weapons, enter the [bold]WEAPON TYPE[/] that will be trade")
    trade_weapon = input(f"     > ")
    trade_weapon = Weapon.find_by_type(trade_weapon.upper())
    return trade_weapon if trade_weapon else console.print("Weapon not found, please check spelling.", style ="error")

def trade_table(trade_char, trade_character_weapon, my_char, my_weapon):
    table = Table("Your Character", "Trade Character", title="TRADE CONFIRMATION")
    table.add_row(f'[name]{my_char.name}[/]', f'[name]{trade_char.name}[/]')
    table.add_row(f'[bold]{my_weapon.type}[/]', f'[bold]{trade_character_weapon.type}[/]')
    console.print(table)

def confirm_trade(trade_char, trade_char_weapon, my_char, my_weapon):
    asterisk_line()
    trade_table(trade_char, trade_char_weapon, my_char, my_weapon)
    console.print(f"[name]{my_char.name}'s[/] [bold]{my_weapon.type}[/] will be exchange for [name]{trade_char.name}'s[/] [bold]{trade_char_weapon.type}[/]")
    console.print('Press "Y" or "y" to confirm the trade or press any other keys to cancel', end="", style="bold underline dark_red")
    confirm = input(': ')
    if confirm == ("y" or "Y"):
        my_weapon.owner_id = trade_char.id
        trade_char_weapon.owner_id = my_char.id
        my_weapon.update()
        trade_char_weapon.update()
        console.print("Trade completed", style ="success")
        from cli import character_menu
        character_menu(my_char)
    else:
        console.print("Trade did not occur.", style ="error")
        console.print("Returning to previous menu", style ="error")
        from cli import trade_menu
        trade_menu(my_char)


def exit_program():
    console.print("Goodbye!", style="bold orange3")
    exit()
