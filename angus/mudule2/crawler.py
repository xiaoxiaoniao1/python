import urllib2
from lxml import html
import os

from utils import dirs
from utils import downloader

basedir = "python_docs"
root = "https://docs.python.org/2.7/"
index = urllib2.urlopen(root).read()

dirs.mkdirs(basedir)

node = html.fromstring(index)
for i in node.xpath("//body//a"):
    url = i.get("href")
    downloader.download(root, url, basedir)
