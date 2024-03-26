# Pour aller plus loin: DHCP et DNS

Dans notre quotidien, nous ne nous préoccupons jamais de savoir quelle est l'adresse IP de notre machine, et nous utilisons des pages web dont le nom est plus humainement lisible que `223.145.172.37`. Ceci est dû à l'utilisation de deux protocoles : `DHCP` et `DNS`.

##  DHCP

!!! info "DHCP"
	DHCP est un acronyme signifiant *Dynamic Host Configuration Protocol*. Il s'agit d'un protocole dont le rôle est de distribuer automatiquement les adresses de configuration IP des machines d'un réseau. Il s'agit en fait de deux programmes, un pour le serveur et un pour les clients.

1. Dans Filius, placer un ordinateur, un switch et un routeur ( avec plus de 3 interfaces).
2. Relier le switch aux deux autres éléments.
3. Configurer le routeur côté switch avec :
	* IP : `192.168.0.254`
	* Masque : `255.255.255.0`
4. Configurer l'ordinateur :
	* Nom : Serveur DHCP
	* IP : `192.168.0.1`
	* Masque : `255.255.255.0`
	* Passerelle : `192.168.0.254`
5. Toujours sur cette machine, dans l'onglet de configuration, cliquer sur `Configuration du service DHCP`.
6. Configurer :
	* Début de plage : `192.168.0.100`
	* Fin de plage : `192.168.0.200`
	* Vérifier que la passerelle et le masque sont conformes au réseau créé.
	* Cocher la case &laquo; Activer le service DHCP &raquo;.
7. Placer maintenant 5 ordinateurs portables, à relier au switch.
8. Pour chacun de ces portables, dans la configuration, cochez :
	* &laquo; Utiliser l'adresse IP comme nom &raquo;
	* &laquo; Adressage automatique par serveur DHCP&raquo;
9. Démarrez  la simulation et observez ce qui se passe.

!!! info "Construction d'un réseau"
	Ainsi, avec un serveur DHCP, il est inutile de configurer une machine classique à la main. C'est ce qui se passe chez vous, votre Box internet donnant automatiquement une configuration, donc une adresse IP. Cette configuration n'est cependant pas absolue, l'adresse IP d'une machine peut varier au sein d'un réseau. En effet, le DHCP distribue sa configuration pour un temps donné, appelé **bail** (pluriel : baux). Au terme du bail, une machine peut donc se voir attribuer une adresse IP différente, et ce de manière transparente.
 
	Cependant, il est parfois nécessaire sur un réseau d'avoir une machine possédant une adresse IP fixe, comme par exemple pour un serveur web, où une passerelle. Dans ce cas on règle l'IP à la main *en dehors de la plage d'adresse du DHCP*.


## Lier noms de domaine et adresses IP : DNS

!!! info "Serveur DNS"
	Dans notre utilisation quotidienne du web, nous tapons des adresses constituées de noms de domaines, par exemple `www.toutatice.fr`. Or nous avons vu qu'un site web n'est qu'un ensemble de fichiers situés sur une machine, et que pour repérer cette machine on utilise son adresse IP.
	
	Il existe donc des machines très importantes sur le réseau, appelées {==**serveurs DNS**==} (acronyme de *Domain Name Server*), qui permettent de faire le lien entre un nom de domaine et une adresse IP.
	
	Ceci impose aux serveurs web d'avoir une IP fixe et non attribuée dynamiquement par un serveur DHCP.
 

1. Créer un deuxième réseau, avec :
	* Un serveur DHCP d'IP `172.16.180.1`, de masque `255.255.255.0`, de passerelle `172.16.180.254`, et de plage d'IP pour le DHCP `172.16.180.100` à `172.16.180.200`.
	*  Un switch ;
	*  3 PC portables avec adressage automatique ;
	*  D'un routeur avec 2 interfaces, dont celle reliée au réseau portant l'IP `172.16.180.254`.

2. Relier les deux routeurs entre eux par un câble.
3. Pour le routeur du réseau `192.168.0.X` :
	* Donner sur l'interface de liaison entre routeurs l'IP `1.0.0.1`, avec un masque `255.0.0.0` ;
	* Dans l'onglet `General`, cocher la case `Routage Automatique` ;
	
4. Pour le routeur du réseau `172.16.180.X` :
	* Donner sur l'interface de liaison entre routeurs l'IP `1.0.0.2`, avec un masque `255.0.0.0` ;
	* Dans l'onglet `General`, cocher la case `Routage Automatique` ;
	
5. Placer un ordinateur que vous relierez par un câble au routeur directement lié au réseau `192.168.0.X`.
6. Configurez cet ordinateur de la manière suivante :
	* Nom : Serveur DNS
	* IP : `10.0.0.100`
	* Masque : `255.255.255.0`
	* Passerelle : `10.0.0.1`
7. Configurez sur le routeur la liaison avec le serveur DNS :
 * IP : `10.0.0.1`
 * Masque : `255.255.255.0`
8. Sur les deux serveurs DHCP, configurez la ligne `Serveur DNS` avec `10.0.0.100`.
9. Lancez la simulation. Testez sur plusieurs machines si les données circulent grâce à la commande `ping`.
10. Sur le serveur DHCP du réseau `192.168.0.X`, installez aussi un serveur web, et démarrez-le.
11. Testez sur au moins un portable de chaque réseau si le serveur web répond, en installant un navigateur web et en demandant dans la barre d'adresse `192.168.0.1`.
	**Si tout fonctionne correctement, nous allons pouvoir changer la manière d'atteindre le serveur web.**
12. Sur le serveur DNS, installez le logiciel `Serveur DNS`, démarrez-le.
13. Ajoutez comme nom de domaine &laquo; supersite.fr &raquo; pour l'adresse IP `192.168.0.1`.
14. Testez alors depuis le navigateur d'un portable, avec l'url `supersite.fr`.

## Pour les plus courageux

Sur un serveur web, installez un éditeur de texte, puis copiez-collez le code HTML du site que vous aviez fabriqué dans la première partie du cours de SNT.

Essayez de le faire s'afficher directement via les portables.


