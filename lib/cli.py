#!/usr/bin/env python3
# lib/cli.py

from helpers import (
    exit_program,
    blankline,
    asterisk_line,
    display_all_characters,
    add_character,
    delete_character
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
    print("  Please select a character:")
    print("     1. Display all characters")
    blankline()
    print("     2. Add a new character")
    blankline()
    print("     3. Exit program")

def display_all_menu(characters):
    while True:
        blankline()
        print("Enter a Character's name for more details or hit 'ENTER' to return to the previous menu.")
        x = 1
        for character in characters:
            character["position"] = x
            blankline()
            print(f'    {character["position"]}', end= ". ")
            print(character)
            blankline()
            x +=1
        # print(f'    {x}. Press "Enter" to return to previous menu')
        choice = input("> ")
        # name = name.lower()

def character_menu(character):
    while True:
        asterisk_line()
        print("Choose an option: ")
        print(f'     1. Update selected {character.name.title()}')
        blankline()
        print(f'     2. Delete seleted character (including all weapons)')
        blankline()
        print(f'     3. Display all weapons')
        blankline()
        print(f'     4. Return to previous menu')

        choice = input("> ")
        if choice == "1":
            print("update")
        elif choice == "2":
            delete_character(character)
        elif choice == "3":
            print("display")
        elif choice == "4":
            print("Returning to previous menu")
            break
        else:
            print("Invalid Choice")




if __name__ == "__main__":
    main()
