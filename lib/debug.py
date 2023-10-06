#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.character import Character
import ipdb

Character.drop_table()
Character.create_table()

bob = Character.create("bob", "adventurer")
print(bob)

sam = Character.create("sam", "mage")
print(sam)

sam.job_class = "swordsman"
sam.update()
print(sam)

print("Delete bob")
bob.delete()
print(bob)

ipdb.set_trace()
