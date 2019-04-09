import os
import sys

def main(dir, filename):
  dirs = os.listdir(dir)
  for d in dirs:
    fullpath = os.path.join(dir, d)
    #print fullpath
    if os.path.isdir(fullpath):
      main(fullpath, filename)
    else:
      if filename in d:
        print "result is %s" % fullpath

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print "please enter dir and filename"
  else:
    print sys.argv[0]
    dir = sys.argv[1]
    filename = sys.argv[2]
    main(dir, filename)
