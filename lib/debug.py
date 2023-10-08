#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.character import Character
from models.weapon import Weapon
import ipdb

def reset_database():
    Character.drop_table()
    Character.create_table()
    Weapon.drop_table()
    Weapon.create_table()

    Character.create("bob", "adventurer")
    Character.create("sam", "mage")
    Character.create("anna", "fencer")
    
    Weapon.create("one handed sword", 4, 1)
    Weapon.create("Magic Wand", 2, 2)
    Weapon.create("Throwing knives",2, 1)
    Weapon.create("Sword", 4, 3)
    

reset_database()

ipdb.set_trace()
