#!/usr/bin/env python3
# lib/cli.py

from helpers import (
    exit_program,
    blankline,
    asterisk_line,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            submain()
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
    print("Please select an option:")
    asterisk_line()
    print("0. Exit the program")
    blankline()
    print("1. Some useful function")

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
