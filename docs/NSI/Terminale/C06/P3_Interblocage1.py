import threading, time
from random import randint

verrou1 = threading.Lock()
verrou2 = threading.Lock()

def f1() :
    time.sleep(randint(0,100)/100)
    verrou1.acquire()
    print("Zone risquée f1.1")
    verrou2.acquire()
    print("Zone risquée f1.2")
    verrou2.release()
    verrou1.release()
    
def f2() :
    verrou2.acquire()
    time.sleep(randint(0,100)/100)
    print("Zone risquée f2.1")
    verrou1.acquire()
    
    print("Zone risquée f2.2")
    verrou1.release()
    verrou2.release()
 
 
t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
 
t1.start()
t2.start()

t1.join()
t2.join()