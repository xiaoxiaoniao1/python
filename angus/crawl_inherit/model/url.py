from datetime import datetime
import json
import traceback

from base import Base

class Url(Base):
    id = None
    url = None
    created_date = None

    def __init__(self, url, id = None, created_date = datetime.now().strftime("%Y-%m-%d %X")):
        #super().__init__()
        self.id = id
        self.url = url
        self.created_date = created_date

    def save(self):
        cur = self.getdb().cursor()
        try:
            sql = "insert into t_url (url, created_date) values ('%s', '%s')" % (self.url, self.created_date)
            print sql
            cur.execute(sql)
            self.getdb().commit()
        except:
            traceback.print_exc()
        finally:
            cur.close()


    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.__str__()
