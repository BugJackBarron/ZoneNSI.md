G = UndirectedGraph()
G.add_vertice("Auvergne-Rhône-Alpes")
G.add_vertice("Bourgogne-Franche-Comté")
G.add_vertice("Bretagne")
G.add_vertice("Centre-Val de Loire")
G.add_vertice("Corse")
G.add_vertice("Grand Est")
G.add_vertice("Guadeloupe")
G.add_vertice("Guyane")
G.add_vertice("Hauts-de-France")
G.add_vertice("Île-de-France")
G.add_vertice("La Réunion")
G.add_vertice("Martinique")
G.add_vertice("Mayotte")
G.add_vertice("Normandie")
G.add_vertice("Nouvelle-Aquitaine")
G.add_vertice("Occitanie")
G.add_vertice("Pays de la Loire")
G.add_vertice("Provence-Alpes-Côte d'Azur")

G.add_edge("Hauts-de-France", "Normandie" )
G.add_edge("Hauts-de-France", "Île-de-France" )
G.add_edge("Hauts-de-France", "Grand Est" )

G.add_edge("Grand Est", "Île-de-France")
G.add_edge("Grand Est", "Bourgogne-Franche-Comté")

G.add_edge("Île-de-France", "Normandie")
G.add_edge("Île-de-France", "Centre-Val de Loire")
G.add_edge("Île-de-France", "Bourgogne-Franche-Comté")

G.add_edge("Bourgogne-Franche-Comté", "Centre-Val de Loire")
G.add_edge("Bourgogne-Franche-Comté", "Auvergne-Rhône-Alpes")

G.add_edge("Auvergne-Rhône-Alpes", "Centre-Val de Loire")
G.add_edge("Auvergne-Rhône-Alpes", "Nouvelle-Aquitaine")
G.add_edge("Auvergne-Rhône-Alpes", "Occitanie")
G.add_edge("Auvergne-Rhône-Alpes", "Provence-Alpes-Côte d'Azur")

G.add_edge("Provence-Alpes-Côte d'Azur", "Occitanie")

G.add_edge("Occitanie", "Nouvelle-Aquitaine")

G.add_edge( "Nouvelle-Aquitaine", "Centre-Val de Loire")
G.add_edge( "Nouvelle-Aquitaine", "Pays de la Loire")

G.add_edge("Pays de la Loire", "Centre-Val de Loire")
G.add_edge("Pays de la Loire", "Normandie")
G.add_edge("Pays de la Loire", "Bretagne")

G.add_edge("Bretagne", "Normandie")

G.add_edge("Normandie", "Centre-Val de Loire")