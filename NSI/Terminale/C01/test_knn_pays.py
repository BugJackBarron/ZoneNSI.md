### Principe :

""" Une série de donnée est constituée d'associations de villes (données par leur latitude/longitude), associées à leur pays d'appartenance.

Une nouvelle donnée latitude/longitude doit renvoyer le pays d'appartenance.
"""

class Location:
    def __init__(self, nom, latitude, longitude, pays):
        self.nom = nom
        self.latitude = latitude
        self.longitude = longitude
        self.pays = pays

    def __str__(self):
        return f"Location(nom={self.nom}, latitude={self.latitude}, longitude={self.longitude}, pays={self.pays})"

    def __repr__(self):
        return self.__str__()
    
    def distance_to(self, other):
        """
        Calcule la distance entre deux locations en utilisant la formule de la distance haversine.
        
        :param other: Une autre instance de la classe Location
        :return: La distance en kilomètres
        """
        # Rayon de la Terre en kilomètres
        R = 6371.0
        
        # Conversion des degrés en radians
        lat1_rad = math.radians(self.latitude)
        lon1_rad = math.radians(self.longitude)
        lat2_rad = math.radians(other.latitude)
        lon2_rad = math.radians(other.longitude)
        
        # Calcul de la différence des coordonnées
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        
        # Formule de la distance haversine
        a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        # Distance en kilomètres
        distance = R * c
        
        return distance


