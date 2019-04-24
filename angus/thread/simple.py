import threading
import time

def worker():
    """thread worker function"""
    time.sleep(2)
    print 'Worker'

for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
