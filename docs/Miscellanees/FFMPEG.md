# FFMPEG

Quelques commandes pour FFMPEG :

# Concaténation de vidéo 

Si les vidéos sont dans le même format :

1. Créer un fichier texte `input.txt` avec la liste des fichiers à concaténer, présentés sous la forme suivante :

    ``` bash
    file 'fichier1.flv'
    file 'fichier2.flv'
    ```
2. Utiliser la commande suivante :

    ```` bash
    ffmpeg -f concat -safe 0 -i input.txt -c copy output.flv
    ````