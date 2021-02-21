import urllib2
from lxml import html
import os
import threading
import time

from utils import dirs
from utils import downloader

basedir = "python_docs"
root = "https://docs.python.org/2.7/"
index = urllib2.urlopen(root).read()

dirs.mkdirs(basedir)

node = html.fromstring(index)

start = time.time()
threads = []
for i in node.xpath("//body//a"):
    url = i.get("href")
    t = threading.Thread(target=downloader.download,args=(root, url, basedir))
    t.start()
    threads.append(t)

#main thread waiting for sub thread
for t in threads:
    t.join()

print "time=%f" % (time.time() - start)
