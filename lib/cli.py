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
    print("  Please choose a character:")
    print("     1. Display all available characters")
    blankline()
    print("     2. Add a new character")
    blankline()
    print("     3. Exit program")



def character_menu(selected_char):
    blankline()
    print(selected_char, end=", \n")
    print(f'    Current weapon(s): {selected_char.weapons()}')
    while True:
        asterisk_line()
        print("Choose an option: ")
        print(f'     1. Update {selected_char.name.title()}')
        blankline()
        print(f'     2. Delete {selected_char.name.title()} (including all weapons)')
        blankline()
        print(f'     3. Display {selected_char.name.title()}\'s weapon(s)')
        blankline()
        print('     4. Return to previous menu')

        choice = input("> ")
        if choice == "1":
            print("update")
        elif choice == "2":
            delete_character(selected_char)
            main()
        elif choice == "3":
            print("display")
        elif choice == "4":
            print("Returning to previous menu")
            break
        else:
            print("Invalid Choice")




if __name__ == "__main__":
    main()
