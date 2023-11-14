# lib/seed.py
from models.__init__ import CONN, CURSOR
from models.character import Character
from models.weapon import Weapon

def seed_database():
    Character.drop_table()
    Character.create_table()
    Weapon.drop_table()
    Weapon.create_table()

    #Create seed data
    bob = Character.create("bob", "Barbarian", 25)
    sam = Character.create("sam", "Mage", 1000)
    anna = Character.create("anna", "Rouge")
    
    Weapon.create("one handed sword", 4, 30, bob.id)
    Weapon.create("magic wand", 2, 20,sam.id)
    Weapon.create("throwing knives",2, 15,bob.id)
    Weapon.create("saber", 4, 45, anna.id)
    

seed_database()
print("Seeded database")