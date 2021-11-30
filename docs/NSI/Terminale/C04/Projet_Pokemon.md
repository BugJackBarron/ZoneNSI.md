# Projet : Base de donnée Web Pokemon.

## Ce qu'il faut faire :

L'objectif est de réaliser un site web HTML5 (HTML/CSS/javascript) permettant d'obtenir les informations importantes sur tous les Pokemons présent dans le fichier `csv` disponible [ici](https://fvergniaud-drive.mytoutatice.cloud/public?sharecode=Rlu994uVRAyg). Cette base de donnée `SQL` sera interrogée au moyen d'un serveur Python `Flask` et du module `sqlite3`.

Il faudra suivre le planning suivant :

1. Extraire les lignes du fichier CSV de manière à construire le fichier de base de donnée (programme python indépendant).
2. Créer un serveur minimal `Flask` permettant  d'accéder à 2 ou 3 *templates* différents : page de recherche de Pokemons, page de résultats de recherche, et éventuellement une page de comparaison entre Pokemons.
3. Créer les templates HTML/Jinja2, en particulier la page de recherche dont le formulaire envoie par une méthode `POST` les données à une route de traitement (voir point suivant).
4. Créer une route spécifique permettant de traiter les données du formulaire de la page de recherche, qui envoie ensuite les données extraites par des ordres `SQL` soit à la page d'affichage du Pokemon sélectionné, soit de nouveau à une page intermédiaire permettant d'obtenir la liste des pokemons correspondant aux critères de recherches sélectionné (génération, type, etc...)
4. Habiller le tout avec du CSS (en dernier !)

## Les tutoriels à suivre :


* le tutoriel `sqlite3` trouvable [ici](https://zestedesavoir.com/tutoriels/1294/des-bases-de-donnees-en-python-avec-sqlite3/).
* Le tutoriel `Flask` trouvable [ici](https://www.kaherecode.com/tutorial/demarrer-avec-flask-un-micro-framework-python).

## Des ressources utiles

Une base de donnée en ligne déjà existante est présente [ici](https://pokemondb.net/). En particulier les images fournies sont toutes de la forme :

````
https://img.pokemondb.net/artwork/large/{nom du pokemon}.jpg
````

