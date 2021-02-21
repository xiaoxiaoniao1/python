import urllib2
import os

dir = "images"

def mkdirs(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)

def download(url):
  mkdirs(dir)

  data = urllib2.urlopen(url).read()
  filename = url.split("/")[-1]
  fullpath = os.path.join(dir, filename)
  with open(fullpath, "wb") as f:
    f.write(data)

if __name__ == "__main__":
  download("https://www.baidu.com/img/bd_logo1.png")
