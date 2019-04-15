import urllib2
from lxml import html
import traceback

response = urllib2.urlopen("http://www.baidu.com")
content = response.read()

doc = html.fromstring(content)
imgs = doc.xpath("//body//img[@class='index-logo-src']")

for img in imgs:
  try:
    url = img.get("src")
    filename = url.split("/")[-1]
    with open(filename, "wb") as f:
      f.write(urllib2.urlopen("http:" + src).read())
  except:
    traceback.print_exc()
