import threading,time

def f():
    import time
    while(True):
        time.sleep(1)
        print("Function out!")

t1 = threading.Thread(target=f)

print("Starting thread")
t1.start()
time.sleep(0.1)
print("Something done")
t1.join()
print("Thread Done")