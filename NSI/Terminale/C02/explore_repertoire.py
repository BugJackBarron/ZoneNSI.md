import os

def explorer_repertoire(repertoire):
    for item in os.listdir(repertoire):
        chemin = os.path.join(repertoire, item)
        if os.path.isdir(chemin):
            explorer_repertoire(chemin)
        else:
            print(chemin)

explorer_repertoire("../")