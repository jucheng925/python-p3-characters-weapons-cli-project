from models.__init__ import CURSOR, CONN
from models.character import Character


class Weapon:
    all = {}

    def __init__(self, type, damage_value, cost_value, owner_id, id =None):
        self.id = id
        self.type = type
        self.damage_value = damage_value
        self.cost_value = cost_value
        self.owner_id = owner_id

    def __repr__(self):
        return f"Weapon: {self.type}, Damage value: {self.damage_value}, Cost value: ${self.cost_value}"
    
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if isinstance(type, str) and len(type):
            self._type = type.upper()
        else:
            raise ValueError("Weapon type must be a non-empty string")
    
    @property
    def damage_value(self):
        return self._damage_value
    
    @damage_value.setter
    def damage_value(self, damage_value):
        if isinstance(damage_value, int) and (10 >= damage_value >= 0):
            self._damage_value = damage_value
        else:
            raise ValueError("Damage Value must be an integer between 0 to 10")
    
    @property
    def cost_value(self):
        return self._cost_value
    
    @cost_value.setter
    def cost_value(self, cost_value):
        if isinstance(cost_value, int) and (50 >= cost_value >= 10):
            self._cost_value = cost_value
        else:
            raise ValueError("Cost value must be an integer between 10 to 50")
    
    @property
    def owner_id(self):
        return self._owner_id
    
    @owner_id.setter
    def owner_id(self, owner_id):
        if isinstance(owner_id, int) and Character.find_by_id(owner_id):
            self._owner_id = owner_id
        else:
            raise ValueError("Owner must reference a character in the database.")
        
    def owner_name(self):
        owner = Character.find_by_id(self.owner_id)
        return owner.name

    #ORM methods
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS weapons (
            id INTEGER PRIMARY KEY,
            type TEXT,
            damage_value INTEGER,
            cost_value INTEGER,
            owner_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES characters(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS weapons;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO weapons (type, damage_value, cost_value, owner_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.type, self.damage_value, self.cost_value, self.owner_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, type, damage_value, cost_value, owner_id):
        weapon = cls(type, damage_value, cost_value, owner_id)
        weapon.save()
        return weapon
    
    def update(self):
        sql = """
            UPDATE weapons
            SET type = ?, damage_value = ?, cost_value = ?, owner_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.type, self.damage_value, self.cost_value, self.owner_id, self.id))
        CONN.commit()


    def delete(self):
        sql = """
            DELETE FROM weapons
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        #delete the dictionary entry using id as the key
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        weapon = cls.all.get(row[0])
        if weapon:
            weapon.type = row[1]
            weapon.damage_value = row[2]
            weapon.cost_value = row[3]
            weapon.owner_id = row[4]
        else:
            weapon = cls(row[1], row[2], row[3], row[4])
            weapon.id = row[0]
            cls.all[weapon.id] = weapon
        return weapon

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM weapons
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM weapons
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_type(cls, type):
        sql = """
            SELECT *
            FROM weapons
            WHERE type is ?
        """
        row = CURSOR.execute(sql, (type,)).fetchone()
        return cls.instance_from_db(row) if row else None

    