import mysql.connector

class Base:
    db = None

    def __init__(self):
        pass

    def getdb(self):
        if not self.db:
            self.db = mysql.connector.connect(
              host="localhost",
              user="root",
              passwd="root",
              database="crawel"
            )
        return self.db
