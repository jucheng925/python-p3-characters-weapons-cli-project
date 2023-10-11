#!/usr/bin/env python3
# lib/cli.py

from helpers import (
    exit_program,
    blankline,
    asterisk_line,
    display_all_characters,
    add_character
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
            print("delete")
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    blankline()
    print(" **Welcome to Game World**")
    asterisk_line() 
    print("  Please select a character:")
    print("     1. Display all characters")
    blankline()
    print("     2. Add a new character")
    blankline()
    print("     3. Delete a character")
    blankline()
    print("     4. Exit program")

def character_menu(character):
    char_menu = True
    while char_menu:
        asterisk_line()
        print("Choose an option: ")
        print(f'     1. Update selected {character.name.title()}')
        blankline()
        print(f'     2. Display all weapons')
        blankline()
        print(f'     3. Return to previous menu')

        choice = input("> ")
        if choice == "1":
            print("update")
        elif choice == "2":
            print("display")
        elif choice == "3":
            print("Returning to previous menu")
            char_menu = False
        else:
            print("Invalid Choice")




if __name__ == "__main__":
    main()
