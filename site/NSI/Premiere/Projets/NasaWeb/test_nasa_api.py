nasa_key="RBGXm5wakyukgagSwBM7Vgb69SiYQMQwVxzlFpYK"
# importation du module webbrowser
import webbrowser
# importation du sous-module MarsRovers du module nasaapi
from nasaapi import MarsRovers
# initialisation de la connexion avec l’API et création de l’ob-jet rovers
rovers = MarsRovers(nasa_key, 100 )
# récupération des données de Curiosity (dictionnaire)
cur = rovers.curiosity()
print(len(cur["photos"]))
# accès à l’URL de la quatrième photo

url= cur['photos'][0]['img_src']

# envoi de l’URL dans le navigateur
webbrowser.open_new_tab(url)
