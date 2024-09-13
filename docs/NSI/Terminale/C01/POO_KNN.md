# Application : POO et KNN

## Algorithme des $K$ Plus Proches Voisins

!!! info "Algorithme KNN"

    L'algorithme dit des {==**$k$ plus proches voisins**==} (*$k$ nearest neighbours*), abrégé en algorithme `KNN`, est un algorithme utilisé en intelligence artificielle, plus particulièrement en apprentissage supervisé.
    

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