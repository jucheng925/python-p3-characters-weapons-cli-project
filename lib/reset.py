from models.__init__ import CONN, CURSOR
from models.character import Character
from models.weapon import Weapon

def reset_database():
    Character.drop_table()
    Character.create_table()
    Weapon.drop_table()
    Weapon.create_table()

reset_database()
print("Reset database")