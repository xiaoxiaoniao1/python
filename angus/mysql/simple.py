import mysql.connector
  
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="hksite"
)

cur = mydb.cursor()
cur.execute("select * from banner")
users = cur.fetchall()

for user in users:
  print user
