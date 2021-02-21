import mysql.connector
from banner import Banner

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
