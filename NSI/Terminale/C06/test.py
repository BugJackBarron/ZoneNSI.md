import time

a = 0
for i in range(100000):
    a += a**3
    time.sleep(0.01)
print("terminé")
