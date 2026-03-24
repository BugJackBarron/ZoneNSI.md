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

# Compressions de vidéo 


## Compression légère et rapide

```
ffmpeg -i input.mp4 -vf scale=1280:-1 -c:v libx264 -preset ultrafast output.mp4
```

## Meilleure compression mais plus lente
```
 ffmpeg -i input.mp4 -vcodec libx265 -crf 32 output.mp4D
```
Plus le paramètre ``crf``est élevé, plus la vidéo sera compressée.

