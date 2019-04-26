import mysql.connector
  
class Banner:
  id = None
  path = None
  weight = None
  menuId = None
  type = None

  def __init__(self, id, path, weight, menuId, type):
    self.id = id
    self.path = path
    self.weight = weight
    self.menuId = menuId
    self.type = type

  def __str__(self):
    return "[id=%s,path=%s,weight=%s,menuId=%s,type=%s]" % (self.id, self.path, self.weight, self.menuId, self.type)

  def __repr__(self):
    return self.__str__()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="hksite"
)

cur = mydb.cursor()
cur.execute("select * from banner")
users = cur.fetchall()

banners = []

for user in users:
  banner = Banner(user[0], user[1], user[2], user[3], user[4])
  banners.append(banner)
  print banner

print banners
