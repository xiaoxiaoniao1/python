from lxml import html
from urllib import parse


class HtmlParser(object):
    
    def parse(self, request_url ,html_code):
        """
        用途: 将html源码转换成html物件
        """
        if html is None:
            return
        else:
            # 将download下来的页面转换成lxml的html物件    
            tree = html.fromstring(html_code)

            # 获取页面下的新链接
            new_urls = self._get_new_urls(request_url,tree)

            return new_urls



    def _get_new_urls(self, request_url , tree):
        """
        传入请求URL原因为使用urljoin方式拼接链接成完整路径
        """
        new_urls = set()
        links = tree.xpath('//a/@href')

        for link in links:
            new_url = link
            new_full_url = parse.urljoin(request_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
