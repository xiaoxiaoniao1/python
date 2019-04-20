
class UrlManager(object):
    """
    用途: 管理爬取的URL
    """
    def __init__(self,enable_external_link=False, bind_domain=None):
        # 建立两个set , 一个储存新url , 放在new_urls的set内 , 当爬过该url后则放入old_urls的set内
        self.old_urls = set()
        self.new_urls = set()
        
        # 若enable_external_link=Flase 则不允许外部链接放入set内 , 避免无限制一直爬外部链接
        # bind_domain则为限制非该domain下的URL一律不写入
        self.enable_external_link = enable_external_link
        self.bind_domain = bind_domain

    def add_new_url(self,url):
        if url is None:
            return
        elif url not in self.new_urls and url not in self.old_urls and self.bind_domain in url:
        # 当不存在新链接集合以及旧链接集合内 , 即为新爬取到的链接 , 且限制这个链接不储存外部域名的链接 , 以防爬到外链程序无法正常结束
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        # 批量添加链接到new_urls内
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0
 
    def get_new_url(self):
        # 使用set方式取出(移除)爬过的元素 , 并新增到old_urls的set内
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url