#!/usr/bin/env python3
# lib/cli.py

from helpers import (
    exit_program,
    blankline,
    asterisk_line,
    display_all_characters,
    add_character,
    delete_character,
    update_character,
    display_weapons,
    add_weapon,
    delete_weapon,
    display_all_weapons,
    trade_partner
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            display_all_characters()
        elif choice == "2":
            add_character()
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    blankline()
    print(" **Welcome to Game World**")
    asterisk_line() 
    print("  Please choose a character:")
    print("     1. Display all available characters")
    blankline()
    print("     2. Add a new character")
    blankline()
    print("     3. Exit program")



def character_menu(selected_char):
    blankline()
    print(selected_char, end=", \n")
    print(f'    Currently has {len(selected_char.weapons())} weapon(s).')
    while True:
        asterisk_line()
        print("Choose an option: ")
        print(f'     1. Update {selected_char.name}')
        blankline()
        print(f'     2. Delete {selected_char.name} (including all current weapons)')
        blankline()
        print(f'     3. Display {selected_char.name}\'s weapon(s)')
        blankline()
        print('     4. Or Press "Enter" to return to previous menu')

        choice = input("> ")
        if choice == "1":
            update_character(selected_char)
        elif choice == "2":
            delete_character(selected_char)
            main()
        elif choice == "3":
            weapon_menu(selected_char)
        elif choice == "4" or choice == "":
            print("Returning to previous menu")
            break
        else:
            print("Invalid Choice")

def weapon_menu(selected_char):
    while True:
        display_weapons(selected_char)
        asterisk_line()
        print("Choose an option: ")
        print('     1. Buy a custom made weapon')
        blankline()
        print('     2. Sell weapon(s)')
        blankline()
        print('     3. Trade weapon with other characters')
        blankline()
        print('     4. Or press "Enter" to previous menu')
        blankline()

        choice = input("> ")
        if choice == "1":
            add_weapon(selected_char)
        elif choice == "2":
            delete_weapon(selected_char)
        elif choice == "3":
            trade_menu(selected_char)
        elif choice == "4" or choice == "":
            print("Returning to previous menu")
            break
        else:
            print("Invalid Choice")

def trade_menu(selected_char):
    while True:
        asterisk_line()
        display_all_weapons()
        trade_name = input("Choose the character you want to trade with or press 'enter' to return to previous menu: ")
        if trade_name == "":
            print("Returning to previous menu")
            blankline()
            break
        else:
            trade_partner(selected_char, trade_name)



if __name__ == "__main__":
    main()
