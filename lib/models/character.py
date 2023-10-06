from __init__ import CURSOR, CONN

class Character:
    def __init__(self, name, job_class, id = None):
        self.id = id
        self.name = name
        self.job_class = job_class

    def __repr__(self):
        return f"<Character {self.id}: {self.name}, {self.job_class}>"


