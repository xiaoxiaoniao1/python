gv = None

def __init__():
    global gv
    gv = "angus"

def test():
    __init__()
    print gv

if __name__ == "__main__":
    test()
