from PIL import Image
from random import randint


###############################################################################
#                                                                                                                                                          #
# Ne pas toucher au code au dessu de cette ligne et jusqu'au prochain commentaire encadré !  #
#                                                                                                                                                          #
###############################################################################


def makeMatrix(img) :
    """ Renvoie la matrice des pixels d'après une image passée en paramètre."""
    width, height = img.size #On récupère les dimensions de l'image
    matrix = [[0]*width for _ in range(height)] # Initialisation de la matrice des pixels
    for y in range(height) :
        for x in range(width) :
            pix = img.getpixel((x,y)) 
            # On élimine le canal alpha si besoin
            matrix[y][x] = pix[:3] if len(pix)>3 else pix        
    return matrix




def extractColor(img,filtreRGB) :
    """Extrait la coloration d'une image en appliqquant un filtre RGB , écrtit sous la forme d'un tuple (x,y,z)
x, y et z sont des réels qui sont compris entre 0 et 2 avec la norme suivante :
- à 0, renvoie la valeur 0 de la composante ;
- à 1, renvoie la valeur actuelle de la composante du pixel ;
- à 2, renvoie la valeur maximale de cette composante ( 255);
"""
    def filtre(v,f) :
        """Fonction interne de filtre par composante"""
        assert 0<=f<=2, "Bad value for filter. Must be beetween 0 and 2"
        return int((255/2-v)*f**2 + (2*v-255/2)*f)
    
    fR,fG,fB = filtreRGB #Décompose (unpack) le filtre selon ses composantes RGB
    width,height = img.size # Récupération de la dimension de l'image originale
    matrix = makeMatrix(img) # récupération de la matrice des pixels
    extractedMatrix = [[0]*width for _ in range(height)] # Initialisation de la matrice obtenue par filtre
    for x in range(width) : #Pour chaque pixel de coordonnées (x;y),
        for y in range(height) :
            R,G,B = matrix[y][x] # récupération des composantes RGB du pixel
            extractedMatrix[y][x] = filtre(R,fR), filtre(G,fG), filtre(B,fB) #Application du filtre sur chaque composante
    return extractedMatrix

def showFromMatrix(matrix) :
    """ Fonction affichant une image selon la matrice des pixels qui lui a été passée en ragument"""
    height = len(matrix)# récupération de la hauteur
    width = len(matrix[0])# récupération de la largeur
    newImg = Image.new('RGB',(width,height)) #création d'une image RGB vierge
    for x in range(width) :
        for y in range(height) :
            newImg.putpixel((x,y),matrix[y][x])#Placement des pixels
    newImg.show() #Montre l'image
    return None

###################################################################################
#                                                                                                                                                                  #
# Les fonctions à modifier se trouvent en dessous, ne pas toucher au code au dessus                         #
#                                                                                                                                                                  #
###################################################################################

def posterize(img) :
    """ Création d'un poster à partir d'une image unique,
    par application de filtres ou de transformations"""
    width, height = img.size
    poster =  [[0]*2*width for _ in range(2*height)]
    M1 = makeMatrix(img)
    MR = extractColor(img,(1,0,0))
    MG = extractColor(img,(0,1,0))
    MB = extractColor(img,(0,0,1))
    for x in range(width) :
        for y in range(height) :
            poster[y][x] = M1[y][x]
            poster[y][x+width] = MR[y][x]
            #A compléter avant la ligne return,  pour obtenir un poster
    return poster    

def negativ(img) :
    """ Construit la matrice du négatif de l'image, en inversant
chaque composante RGB par la formule 255-x, où
x est la valeur du pixel"""
    width,height = img.size #On récupère les dimensions de l'image
    matrix = makeMatrix(img) #récupération de la matrice des pixels
    negat =  [[0]*width for _ in range(height)] # Initialisation de la matrice du  négatif
    for x in range(width) :
        for y in range(height) :
            R,G,B = matrix[y][x] # récupération des composantes RGB de la matrice initiale
            negat[y][x] = 255-R,255-G,255-B # Affectation des négatifs pour la matrice finale
    return negat   
    


if __name__ == "__main__" :
    originalImg = Image.open("Pavie.png").convert('RGB') # Ouvertur de l'image choisie
    matrix = makeMatrix(originalImg)
    showFromMatrix(matrix)
    #newMatrix = extractColor(originalImg,(0,1,0))
    #showFromMatrix(newMatrix)
    #poster = posterize(originalImg)
    #showFromMatrix(poster)
    #neg = negativ(originalImg)
    #showFromMatrix(neg)
    
    