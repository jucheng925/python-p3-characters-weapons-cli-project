from models.__init__ import CURSOR, CONN

class Weapon:
    all = {}
    
    def __init__(self, type, damage_value, owner_id=None, id =None):
        self.id = id
        self.type = type
        self.damage_value = damage_value
        self.owner_id = owner_id

    def __repr__(self):
        return f"<Weapon {self.id}: {self.type}, {self.damage_value}, {self.owner_id}"