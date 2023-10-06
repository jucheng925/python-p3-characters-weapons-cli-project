from models.__init__ import CURSOR, CONN

class Character:
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


    

    

