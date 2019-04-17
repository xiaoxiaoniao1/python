import urllib2
import os

dir = "picture"

def mkdirs(dir):
  if not os.path.exists(dir):
   os.makedirs(dir)

def download(url):
  mkdirs(dir)

  source = urllib2.urlopen(url).read()
  filename = url.split("/")[-1]
  filepath = os.path.join(dir, filename)
  with open(filepath, "wb") as f:
    f.write(source)

if __name__ == "__main__":
  download("https://box.bdimg.com/static/fisp_static/common/img/searchbox/logo_news_276_88_1f9876a.png")
