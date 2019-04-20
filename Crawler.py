from UrlManager import UrlManager
from HtmlParser import HtmlParser
from HtmlDownloader import HtmlDownloader

class Crawler(object):
    """
    用途: 主要爬虫程序
    """
    def __init__(self, bind_domain):
        
        # 建立管理爬取URL的物件 , 用于记录已经爬过的URL
        self.urlManager = UrlManager(enable_external_link=False, bind_domain=bind_domain)

        # 建立请求链接的物件 
        self.downloader = HtmlDownloader()

        # 建立转换Html源码成lxml.html物件 , 获取新的链接
        self.parser = HtmlParser()

    def craw(self,url):
        
        # 加入根页面
        self.urlManager.add_new_url(root_url)

        # 查询Manager内储存url的集合
        while self.urlManager.has_new_url():

            # 获取新的url链接
            request_url = self.urlManager.get_new_url()
            print("目前请求{0}".format(request_url))

            # 下载页面
            html_content = self.downloader.downlaod(request_url)

            # 转换html后筛选出所有a记录并且取得新的链接
            new_urls = self.parser.parse(request_url,html_content)

            # 加入链接到管理器
            self.urlManager.add_new_urls(new_urls)



if __name__=='__main__':
    
    protocal = 'https'
    domain_name ='docs.python.org'
    version ='2.7'
    root_url = "{0}://{1}/{2}/".format(protocal,domain_name,version)

    # 建立物件
    crawler = Crawler(bind_domain = domain_name )
    
    # 开始爬曲
    crawler.craw(root_url)