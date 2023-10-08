#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.character import Character
import ipdb

def reset_database():
    Character.drop_table()
    Character.create_table()

    Character.create("bob", "adventurer")
    Character.create("sam", "mage")
    Character.create("anna", "fencer")
    

reset_database()

ipdb.set_trace()
