import os
import sys

def main(dir, content):
  dirs = os.listdir(dir)
  for d in dirs:
    fullpath = os.path.join(dir, d)
    if os.path.isdir(fullpath):
      main(fullpath, content)
    else:
      if d.endswith(".pdf") or d.endswith(".mp4"):
        continue
      else:
        with open(fullpath, "r") as f:
          for line in f.readlines():
            if content in line:
              print "result is %s" % fullpath
              break

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print "please enter dir and filename"
  else:
    dir = sys.argv[1]
    content = sys.argv[2]
    main(dir, content)
