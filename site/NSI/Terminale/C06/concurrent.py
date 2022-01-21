from threading import Thread
from time import sleep

def f1():
    for _ in range(5):
        print("Bonjour !")
        sleep(0.01)

def f2():
    for _ in range(5):
        print("Ça va ?")
        sleep(0.01)

if __name__ == "__main__" :
    p1 = Thread(target=f1)
    p2 = Thread(target=f2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()