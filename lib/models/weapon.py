from models.__init__ import CURSOR, CONN
from models.character import Character

class Weapon:
    all = {}

    def __init__(self, type, damage_value, owner_id, id =None):
        self.id = id
        self.type = type
        self.damage_value = damage_value
        self.owner_id = owner_id

    def __repr__(self):
        return (
            f"<Weapon {self.id}: {self.type}, {self.damage_value}, " +
            f"Owner ID: {self.owner_id}>"
        )
    
    #ORM methods
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS weapons (
            id INTEGER PRIMARY KEY,
            type TEXT,
            damage_value INTEGER,
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
            INSERT INTO weapons (type, damage_value, owner_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.type, self.damage_value, self.owner_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, type, damage_value, owner_id):
        weapon = cls(type, damage_value, owner_id)
        weapon.save()
        return weapon
    
    def update(self):
        sql = """
            UPDATE weapons
            SET type = ?, damage_value = ?, owner_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.type, self.damage_value, self.owner_id, self.id))
        CONN.commit()


    def delete(self):
        sql = """
            DELETE FROM characters
            where id = ?
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
            weapon.owner_id = row[3]
        else:
            weapon = cls(row[1], row[2], row[3])
            weapon.id = row[0]
            cls.all[weapon.id] = weapon

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM weapons
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]