from urllib import request

class HtmlDownloader(object):
    """
    用途: 请求指定Url , 返回请求页面html
    """
    def downlaod(self,url):
        if url is None:
            return None
        else:
            try:
                response = request.urlopen(url)
                if response.getcode() == 200:
                    return response.read()
                else:
                    return None
            except Exception as e:
                print("发生例外: {0}".format(e))
