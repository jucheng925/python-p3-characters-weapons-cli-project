#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.character import Character
import ipdb

Character.drop_table()
Character.create_table()

bob = Character("bob", "adventurer")
print(bob)

bob.save()
print(bob)

sam = Character("sam", "mage")
print(sam)

sam.save()
print(sam)

ipdb.set_trace()
