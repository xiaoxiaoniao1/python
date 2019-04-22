import urllib2
import os
import dirs

def download(root, url, basedir):
    if url.endswith(".html"):
        content = urllib2.urlopen(root + url).read()

        arr = url.split("/")
        if len(arr) > 1:
            filename = arr[-1]
            subdir = "/".join(arr[0:-1])
            print subdir, filename

            fulldir = dirs.mkdirs(basedir, subdir)
            fullpath = os.path.join(fulldir, filename)
            with open(fullpath, "w") as f:
                f.write(content)
        else:
            filename = arr[0]
            print filename
            fullpath = os.path.join(basedir, filename)
            with open(fullpath, "w") as f:
                f.write(content)

if __name__ == "__main__":
  download("https://www.baidu.com/img/bd_logo1.png")
