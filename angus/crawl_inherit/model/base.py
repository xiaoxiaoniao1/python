import mysql.connector

#db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="crawel")
db = None

class Base:
    # use singleton pattern to initize db
    def __init__(self):
        global db
        if not db:
            db = mysql.connector.connect(
              host="localhost",
              user="root",
              passwd="root",
              database="crawel"
            )
        return db

    def getdb(self):
        # can not call self.__init__() here, because it would be called by Url
        #self.__init__()
        global db
        return db
