from models.__init__ import CONN, CURSOR
from models.character import Character
from models.weapon import Weapon

def seed_database():
    Character.drop_table()
    Character.create_table()
    Weapon.drop_table()
    Weapon.create_table()

    #Create seed data
    bob = Character.create("Bob", "adventurer")
    sam = Character.create("Sam", "mage")
    anna = Character.create("Anna", "fencer")
    
    Weapon.create("one handed sword", 4, bob.id)
    Weapon.create("magic wand", 2, sam.id)
    Weapon.create("throwing knives",2, bob.id)
    Weapon.create("saber", 4, anna.id)
    

seed_database()
print("Seeded database")