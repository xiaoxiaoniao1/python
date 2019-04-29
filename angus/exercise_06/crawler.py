import urllib2
from lxml import html
import os
import threading
import time
import mysql.connector

from utils import dirs
from utils import downloader
from url import Url

basedir = "python_docs"
root = "https://docs.python.org/2.7/"
index = urllib2.urlopen(root).read()

dirs.mkdirs(basedir)

node = html.fromstring(index)

start = time.time()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="crawel"
)

cur = mydb.cursor()

#threads = []
for i in node.xpath("//body//a"):
    url = i.get("href")
    ourl = Url(url)
    sql = "insert into t_url (url, created_date) values ('%s', '%s')" % (ourl.url, ourl.created_date)
    print sql
    cur.execute(sql)
    #t = threading.Thread(target=downloader.download,args=(root, url, basedir))
    #t.start()
    #threads.append(t)

mydb.commit()
cur.close()
mydb.close()

#main thread waiting for sub thread
#for t in threads:
#    t.join()

print "time=%f" % (time.time() - start)
