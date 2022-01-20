from threading import Thread
from time import sleep

# Variable globale
compteur = 0 
limite = 100

def calcul():
    """Une fonction qui fait un calcul"""
    global compteur
    for c in range(limite):
        temp = compteur
        # simule un traitement nécessitant des calculs
        sleep(0.000000001)
        compteur = temp + 1

compteur = 0
mesThreads = []
for i in range(4): # Lance en parallèle 4 exécutions de calcul
    p = Thread(target = calcul)
    p.start()      # Lance calcul dans un processus léger à part.
    mesThreads.append(p)

# On attend la fin de l'exécution des threads.
for p in mesThreads :
        p.join()

print(compteur)