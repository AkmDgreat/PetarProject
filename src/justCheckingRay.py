import threading
import time

def do_something():
    while True:
        print("thread 1")
        #time.sleep(5)
def do_something2():
    while True:
        print("thread 2")
        #time.sleep(1)
if __name__ == "__main__":
    proc = threading.Thread(target = do_something)
    proc.start()
    proc2 = threading.Thread(target= do_something2)
    proc2.start()