# Sécurisation des communications

## Rappels : communication sur internet

Que se passe-t-il lorsque nous tapons dans la barre d'adresse de Firefox une URL, telle que `http://www.zonensi.fr/` ? Entre le cours de SNT de seconde, et celui de NSI, nous pouvons décrire l'enchainement des communications ainsi :

1. L'URL est décodée par le navigateur, qui isole :
    * le protocole utilisé : `HTTP`
    * le nom de domaine : `www.zonensi.fr`
    * le chemin vers la ressource : `/`, la racine du site.
2. Le navigateur effectue une résolution de nom, soit en se connectant à un serveur `DNS`, soit dans son propre cache `DNS`, ce qui lui donne l'adresse `IP` de la ressource cherchée.
3. Le navigateur peut établir une connexion `TCP` vers l'adresse `IP`, via un [handshaking en trois temps](https://fr.wikipedia.org/wiki/Three-way_handshake#Fonctionnement){: target="_blank"}, comme montré sur l'image ci-dessous :

    ![TCP Handshake](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Tcp_normal_2.png/800px-Tcp_normal_2.png){: style="width:30%; margin:auto;display:block;background-color: #d2dce0;"}

4. Une fois la connexion établie, client et serveur échangent des données en utilisant le protocole `HTTP`, tout en découpant les données en paquets `TCP`, eux-mêmes encapsulés dans des paquets `IP` (on pourra se rappeler du modèle `OSI`).

    ![Encapsulation](http://www.monlyceenumerique.fr/nsi_premiere/archios_arse/img/arse3_couche_internet.png){: style="width:60%; margin:auto;display:block;background-color: #d2dce0;"}

5. Les paquets sont transmis de routeurs en routeurs, en étant à chaque fois désencapsulés pour inscrire l'adresse `IP` du prochain routeur.

    ![Routage](http://www.monlyceenumerique.fr/nsi_premiere/archios_arse/img/arse3_chemin_transmission_fin.png){: style="width:60%; margin:auto;display:block;background-color: #d2dce0;"}



!!! warning "Des limites"

    Ce système, en place depuis l'invention de `TCP/IP` dans les années 1970, a vu l'intégration de chaque nouveau protocole (`FTP`, `SMTP`, etc) au sein de la couche application. Mais avec la démocratisation d'Internet, des problèmes sont rapidement apparus : si on utilise tel quel le modèle écrit ci-dessus pour effectuer des opérations bancaires ou échanger des données confidentielles, 


## Quelques définitions nécessaires

!!! infos "Cryptographie"
    La {==**cryptographie**==} est une discipline veillant à protéger des messages (pour en assurer la confidentialité, l'authenticité et l'intégrité), par l'intermédiaire de {==**clés de chiffrements**==}.

    La cryptographie est utilisée depuis au moins l'antiquité.

    Une méthode de transformation d'un message est appelée {==**chiffrement**==}, et un chiffrement se fait par l'intermédiaire de règles appelées 

!!! infos "Cryptanalyse"
    ...


## Chiffrement symétriques

###