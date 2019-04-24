import os
  
def mkdirs(*args):
  fulldir = os.path.join(*args)

  if not os.path.exists(fulldir):
    os.makedirs(fulldir)
  return fulldir
