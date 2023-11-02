#!/usr/bin/env python3
# lib/cli.py

from helpers import (
    exit_program,
    blankline,
    asterisk_line,
    display_all_characters,
    validate_selection,
    add_character,
    delete_character,
    update_character,
    display_weapons,
    add_weapon,
    delete_weapon,
    display_all_weapons,
    trade_partner,
    console
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            select_char_menu()
        elif choice == "2":
            add_character()
        elif choice == "3":
            exit_program()
        else:
            console.print("Invalid Choice", style="error")


def menu():
    blankline()
    console.print(" ***Welcome to Game World***", style="underline bold chartreuse3")
    blankline()
    asterisk_line() 
    console.print("  [bold]Character Menu:[/] please choose a character:")
    blankline()
    console.print("     [italic]1. Display all available characters[/]")
    blankline()
    console.print("     [italic]2. Add a new character[/]")
    blankline()
    console.print("     [italic]3. Exit program[/]")

def select_char_menu():
    while True:
        display_all_characters()
        blankline()
        console.print("Type the name of the character for more details or press 'Enter' to return to the previous menu.", style="bold")
        choice = input(" > ")
        if choice == "":
            console.print("Returning to previous menu", style="error")
            main()
        else:
            validate_selection(choice)


def character_menu(selected_char):
    while True:
        blankline()
        console.print(f' [success] {selected_char}[/]')
        console.print(f'    [success]Currently has {len(selected_char.weapons())} weapon(s).[/]')
        blankline()
        asterisk_line()
        console.print("Choose an option: ", style="bold")
        console.print(f'     [italic]1. Update [name]{selected_char.name}[/][/]')
        blankline()
        console.print(f'     [italic]2. Delete [name]{selected_char.name}[/] (and associated weapons)[/]')
        blankline()
        console.print(f'     3. Display [name]{selected_char.name}\'s[/] weapons', style = "italic")
        blankline()
        console.print('     [italic]4. Or Press "Enter" to return to previous menu[/]')

        choice = input("> ")
        if choice == "1":
            update_character(selected_char)
        elif choice == "2":
            delete_character(selected_char)
            main()
        elif choice == "3":
            weapon_menu(selected_char)
        elif choice == "4" or choice == "":
            console.print("Returning to previous menu", style="error")
            select_char_menu()
        else:
            console.print("Invalid Choice", style="error")

def weapon_menu(selected_char):
    while True:
        display_weapons(selected_char)
        asterisk_line()
        console.print("Choose an option: ", style="bold")
        console.print('     [italic]1. Buy a custom made weapon[/]')
        blankline()
        console.print('     [italic]2. Sell weapon[/]')
        blankline()
        console.print('     [italic]3. Trade weapon with other characters[/]')
        blankline()
        console.print('     [italic]4. Or press "Enter" for previous menu[/]')
        blankline()

        choice = input("> ")
        if choice == "1":
            add_weapon(selected_char)
        elif choice == "2":
            delete_weapon(selected_char)
        elif choice == "3":
            trade_menu(selected_char)
        elif choice == "4" or choice == "":
            console.print("Returning to previous menu", style="error")
            character_menu(selected_char)
        else:
            console.print("Invalid Choice", style="error")

def trade_menu(selected_char):
    while True:
        if not selected_char.weapons():
            console.print(f'[name]{selected_char.name}[/] [error]has no weapons and can not trade. Buy a weapon instead.[/]')
            blankline()
            break
        else:
            asterisk_line()
            display_all_weapons()
            console.print('Choose the character you want to trade with or press "Enter" to return to previous menu', style="bold")
            trade_part = input("        > ")
            if trade_part == "":
                console.print("Returning to previous menu", style="error")
                blankline()
                weapon_menu(selected_char)
            else:
                trade_partner(selected_char, trade_part)



if __name__ == "__main__":
    main()
