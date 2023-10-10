#!/usr/bin/env python3
# lib/cli.py

from helpers import (
    exit_program,
    blankline,
    asterisk_line,
    helper_1
)


def main():
    choice = 0
    while choice < 4:
        menu()
        choice = int(input("> "))
        if choice == 1:
            print("display")
        elif choice == 2:
            print("add")
        elif choice == 3:
            print("delete")
        elif choice == 4:
            exit_program()
        else:
            print("Invalid choice")

def submain():
    while True:
        submenu()
        choice = input("> ")
        print(choice)
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
            prev_menu()
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

def submenu():
    print("Select suboption:")
    asterisk_line()
    asterisk_line()
    print("option 1")
    print("option 2")

def prev_menu():
    choice = input("Go back to previous menu? (Y/N): ")
    if choice == "Y":
        menu()
    else:
        exit_program()


if __name__ == "__main__":
    main()
