import urllib2
import os
from lxml import html

datadir = "learn05"

docs = "https://docs.python.org/3.7/"

ht = urllib2.urlopen(docs).read()

if os.path.exists(datadir):
  print "datadir exists"
else:
  os.makedirs(datadir)

node = html.fromstring(ht)

for i in node.xpath("//body//a"):
  url = i.get("href")
  if url.endswith(".html"):
    content = urllib2.urlopen(docs + url).read()

    ar = url.split("/")
    if len(ar) > 1:
      filename = ar[-1]
      subdir = "/".join(ar[0:-1])
      print filename, subdir

      fulldir = os.path.join(datadir, subdir)
      if not os.path.exists(fulldir):
        os.makedirs(fulldir)

      fullpath = os.path.join(fulldir, filename)
      with open(fullpath, "w") as f:
       f.write(content)

    else:
      filename = ar[0]
      print filename
      fullpath = os.path.join(datadir, filename)
      with open(fullpath, "w") as f:
        f.write(content)
