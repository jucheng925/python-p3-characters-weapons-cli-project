from models.__init__ import CURSOR, CONN

class Character:
    all = {}

    def __init__(self, name, job_class, id = None):
        self.id = id
        self.name = name
        self.job_class = job_class

    def __repr__(self):
        return f"<Character {self.id}: {self.name}, {self.job_class}>"


    #ORM methods
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY,
            name TEXT,
            job_class TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS characters;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO characters (name, job_class)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.job_class))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    
    @classmethod
    def create(cls, name, job_class):
        character = cls(name, job_class)
        character.save()
        return character
    
    
    def update(self):
        sql = """
            UPDATE characters
            SET name = ?, job_class = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.job_class, self.id))
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

    ##mapping database row to python object
    @classmethod
    def instance_from_db(cls, row):
        character = cls.all.get(row[0])
        if character:
            character.name = row[1]
            character.job_class = row[2]
        else:
            character = cls(row[1], row[2])
            character.id = row[0]
            character.all[character.id] = character
        return character
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM characters
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM characters
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM characters
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def weapons(self):
        from weapon import Weapon
        sql = """
            SELECT * FROM weapons
            WHERE owner_id = ?
        """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        return [Weapon.instance_from_db(row) for row in rows]
    

    
    


    
    

