import urllib2
from lxml import html
import os

basedir = "python_docs"
root = "https://docs.python.org/2.7/"
index = urllib2.urlopen(root).read()

if not os.path.exists(basedir):
    os.makedirs(basedir)

node = html.fromstring(index)
for i in node.xpath("//body//a"):
    url = i.get("href")
    if url.endswith(".html"):
        content = urllib2.urlopen(root + url).read()

        arr = url.split("/")
        if len(arr) > 1:
            filename = arr[-1]
            subdir = "/".join(arr[0:-1])
            print filename, subdir

            fulldir = os.path.join(basedir, subdir)
            if not os.path.exists(fulldir):
                os.makedirs(fulldir)

            fullpath = os.path.join(fulldir, filename)
            with open(fullpath, "w") as f:
                f.write(content)
        else:
            filename = arr[0]
            print filename
            fullpath = os.path.join(basedir, filename)
            with open(fullpath, "w") as f:
                f.write(content)
