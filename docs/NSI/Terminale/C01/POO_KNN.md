# Application : POO et KNN

## Algorithme des $K$ Plus Proches Voisins

!!! info "Algorithme KNN"

    L'algorithme dit des {==**$k$ plus proches voisins**==} (*$k$ nearest neighbours*), abrégé en algorithme `KNN`, est un algorithme utilisé en intelligence artificielle, plus particulièrement en apprentissage supervisé. C'est un algorithme utilisé entre autres pour *classifier* des données connaissant des exemples déjà classés.
    
    Le principe est le suivant :

    * un jeu des données d'apprentissage est fourni, c'est-à-dire un ensemble de couples `(Données, Classe)` ;
    * Pour déterminer la *classe* d'une nouvelle d'un nouvel objet à partir de ses données, on va utiliser une formule de distance, et calculer la distance entre l'objet à classer et tous les objets du jeu de données. Une fois ces calculs effectués, on classera l'objet comme ayant la **classe majoritaire** parmi ses $k$ plus proches voisins, où $k$ est un entier déterminé à l'avance.

!!! example "Classement d'un personnage de MMORPG"
    On dispose dans un jeu de deux classes de personnages : Magicien et Guerrier.
    les personnages sont représentés par deux caractéristiques : la force et l'intelligence. On représente dans un repère les personnages de la manière suivante :
    
    * un Magicien par un carré bleu ;
    * un Guerrier par un rond rouge.

    On souhaiterait attribuer automatiquement une classe à un nouveau personnage dont la force est de 25 et l'intelligence de 26, représenté par une étoile verte sur le schéma ci-dessous, en utilisant la distance euclidienne classique :

    ![KNN.png](KNN.png){: style="width:50%; margin:auto;display:block;background-color: #d2dce0;"}

    Dans l'exemple ci-dessus, on constate que La valeur de $k$ influence grandement la classe obtenue :

    * Avec $k=3$, c'est-à-dire les trois plus proche voisins, on obtiens deux carrés et un rond, donc la classe obtenue est **Magicien**.
    * Avec $k=5$, on obtient 2 carrés et trois ronds, donc la classe obtenue est Guerrier.

!!! warning "Importance des paramètres"

    En tant qu'algorithme d'apprentissage supervisé, l'algorithme des KNN peut -être particulièrement efficace, mais il faut prendre conscience de l'impact de certains paramètres :


    * la taille et la pertinence du {==**dataset**==} (jeu de données) est un facteur primordial ;
    * la formule de la distance utilisée importe aussi beaucoup. C'est elle qui au final détermine les voisins les plus proches, et il faut parfois pondérer certains éléments pour obtenir une distance significative ;
    *  la valeur de $k$ doit être choisie avec soin : trop petite, elle ne permet pas une prise en compte de variations, mal choisie elle peut amener à des indécisions (avec $k=4$ dans l'exemple précédent, il était impossible de décider), trop grande et le choix est alors seulement liée à la taille du dataset.

    Il est donc souvent nécessaire d'ajuster ces différents paramètres pour obtenir une classification qui soit efficace.


## Application : Classifications de Patients

``` python

class Patient:
    def __init__(self, nom, age, pression, cholesterol, diagnostic=None):
        self.nom = nom
        self.age = age
        self.pression = pression
        self.cholesterol = cholesterol
        self.diagnostic = diagnostic

    def afficher_patient(self):
        return f"Patient {self.nom}, Âge: {self.age}, Pression: {self.pression}, Cholestérol: {self.cholesterol}, Diagnostic: {self.diagnostic}"


class DiagnostiqueurKNN:
    def __init__(self, patients, k=3):
        self.patients = patients
        self.k = k

    def distance(self, patient1, patient2):
        return abs(patient1.pression - patient2.pression) + abs(patient1.cholesterol - patient2.cholesterol)

    def classer_patient(self, nouveau_patient):
        distances = [(patient, self.distance(nouveau_patient, patient)) for patient in self.patients]
        distances = sorted(distances, key=lambda x: x[1])[:self.k]
        diagnostics = [patient[0].diagnostic for patient in distances]
        return max(set(diagnostics), key=diagnostics.count)


# Exemple d'utilisation
patients = [
    Patient("Alice", 45, 120, 200, "Sain"),
    Patient("Bob", 50, 140, 220, "À risque"),
    Patient("Charlie", 55, 130, 210, "Sain"),
    Patient("David", 60, 150, 230, "À risque"),
]

diagnostiqueur = DiagnostiqueurKNN(patients)
nouveau_patient = Patient("Eve", 52, 135, 215)
diagnostic = diagnostiqueur.classer_patient(nouveau_patient)
nouveau_patient.diagnostic = diagnostic
print(nouveau_patient.afficher_patient())
```