# -*- coding:utf-8 -*-
import urllib2
import lxml.html
def loadPage(url):
    page=urllib2.urlopen(url)
    html=page.read()
    ht=html
    en = lxml.html.fromstring(html)
    result = en.xpath("//img[contains(@class,'index-logo-srcnew')]")
    print len(result)
    for i in range(len(result)):
        with open(str(i)+'.png','wb') as f:
            picture=result[i].get('src')

            f.write(urllib2.urlopen('http:'+picture).read())


if __name__ == "__main__":
    url = "http://www.baidu.com"
    loadPage(url)
