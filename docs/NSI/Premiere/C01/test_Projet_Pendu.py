from random import choice


def choixMot(fichier) :
    listeMots = []
    with open(fichier,'r') as file :
        return choice([m for m in file.readlines()])
    
def main() :
    motATrouver = choixMot('listeMots.txt')
    lettresUtilisees = ''
    continuer = True
    while continuer :
        ...
            
if __name__ == "__main__" :
    
            
            