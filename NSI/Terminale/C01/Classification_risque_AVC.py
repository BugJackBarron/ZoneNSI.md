class Patient :
    def __init__(self, prenom : str, sexe : str, age : int, pression : int, cholesterol : int , fumeur : bool, diagnostic : str = None) :
        self.prenom = prenom
        self.sexe = sexe
        self.age = age
        self.pression = pression
        self.cholesterol = cholesterol
        self.fumeur = fumeur
        self.diagnostic = diagnostic
        
    def __repr__(self) -> str :
        return f"""
    {self.prenom}, {self.sexe}, {self.age} ans :
    -> P.A.S. : {self.pression}
    -> H.D.L : {self.cholesterol}
    -> fumeur  : {'Oui' if self.fumeur else 'Non'}
    =======> Diagnostic : {self.diagnostic}
    
    """
    
    
class DiagnostiqueurKNN :
    def __init__(self, patients_connus : list, k :int = 3) :
        self.patients_connus = patients_connus
        self.k = k
        
        
    """ def distance(self, patient_1 : Patient, patient_2 : Patient) :
        return (patient_1.pression - patient_2.pression)**2 + (patient_1.cholesterol-patient_2.cholesterol)**2 """
        
    def distance(self, patient_1 : Patient, patient_2 : Patient, wp = 1, wc = 0.8, wa = 0.5, ws = 0.2) :
        def normalize (x1, x2) :
            return ((x1-x2)/max(x1,x2))**2
        S1 = 1 if patient_1.sexe =='Homme' else 0
        S2 = 1 if patient_2.sexe =='Homme' else 0
        return wp*normalize(patient_1.pression, patient_2.pression
                            ) + wc*normalize(patient_1.cholesterol, patient_2.cholesterol
                                             ) + wa*normalize(patient_1.age, patient_2.age) +ws * (S1-S2)**2 
    
    def classer_patient(self, patient) :
        distances = {pc :self.distance(patient, pc) for pc in self.patients_connus}
        knn = sorted(distances.keys(), key = lambda x : distances[x])[:self.k]
        risques = {}
        
        for patient in knn :
            if patient.diagnostic in risques :
                risques[patient.diagnostic] +=1
            else :
                risques[patient.diagnostic]  = 1
        print(risques)
        return max(risques, key = lambda x: risques[x])
        
        
    
    
patients_connus = [
    Patient("Paul", "Homme", 45, 130, 210, True, "À risque"),
    Patient("Jean", "Homme", 50, 145, 240, False, "Sain"),
    Patient("Robert", "Homme", 55, 160, 260, True, "À risque"),
    Patient("David", "Homme", 35, 120, 180, False, "Sain"),
    Patient("Marc", "Homme", 60, 170, 280, True, "À risque"),
    Patient("Luc", "Homme", 40, 135, 220, False, "Sain"),
    Patient("Claire", "Femme", 30, 115, 190, False, "Sain"),
    Patient("Marie", "Femme", 55, 150, 240, True, "À risque"),
    Patient("Sophie", "Femme", 50, 140, 230, True, "À risque"),
    Patient("Julie", "Femme", 45, 130, 210, False, "Sain")
]