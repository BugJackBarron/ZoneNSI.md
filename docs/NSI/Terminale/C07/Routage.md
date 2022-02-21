# Protocoles de routages

Il est fortement conseillé d'avoir repris le cours de [SNT sur les réseaux](../../../../SNT/Reseaux/TCP_IP/) avant d'entamer cette partie.

## Chacun sa route...

### La commande `ping`

Nous connaissons la commande `ping` qui permet d'envoyer des paquets `ICMP` (*Internet Control Message Protocol*) à une adresse de destination. Le but de ce protocole `ICMP` est d'échanger des informations d'états et des messages d'erreurs. Par exemple, le commande `ping` sur l'adresse `8.8.8.8` (DNS de Google), donne depuis chez moi :

![Ping1.png](Ping1.png){: style="width:60%; margin:auto;display:block;background-color: #546d78;"}

Parmi les informations données par la commande `ping`, on a bien entendu le temps d'aller-retour entre l'ordinateur émetteur et l'ordinateur cible, le nombre de paquets envoyés et reçus, mais aussi une information dont nous n'avons pas encore parlé : le `TTL` (*Time To Live* - attention seulement en IPV4).

!!! abstract "TTL"

	La durée de vie `TTL` correspond à la durée pendant laquelle un paquet de données est valide. 
	La valeur initiale est au maximum de 255. Habituellement, les implémentations ont une TTL initiale de 31, 63 ou 127. Pour chaque nœud de réseau que passe le paquet de données, le TTL est décrémenté de 1. On parle dans ce cas de {==**hops**==}. Si la TTL baisse jusque 0, le paquet de données est rejeté.

	En pratique, le TTL qui vous est communiqué correspond généralement à la **valeur initiale** de l’ordinateur distant, dont on aura **déduit le nombre de passages par un routeur**.

	Si vous avez par exemple un TTL de 58, vous pouvez en déduire que le paquet de réponse avait été émis avec une valeur initiale de 63, et que sur le chemin du retour, il est passé par 5 machines.
	
	!!! warning
		Attention, nous ne sommes pas certain de ce point... Il pourrait tout aussi bien avoir été émis avec une valeur initiale de 127, et donc être passé par 69 routeurs... Le TTL n'est donc qu'une indication...
		
Dans notre exemple, on peut supposer qu'avec un TTL de 119, on est passé par 8 machines pour aller de chez moi jusqu'au DNS de Google.

!!! question "Tester `ping`"

	=== "Enoncé"
		1. Depuis l'invite de commande de windows  :
			1. Tester la commande `ping 8.8.8.8`. Quel est le TTL, que peut-on supposer ?
			2. Tester la commande `ping -4 www.zonensi.fr`. Que se passe-t-il ?
			3. Tester la commande `ping -6 www.zonensi.fr`. Que se passe-t-il ?
		2. Depuis l'invite de commande Linux de [JupyterHub](https://zonensi.fr:8443){: target="_blank"} :
			1. Tester la commande `ping 8.8.8.8`. Quelle différence y-a-t'il avec la commande windows ?
			2. Tester la commande `ping -c 5 8.8.8.8`. Que se passe-t-il ?
			3. Tester la commande `ping -t 5 8.8.8.8`. Que se passe-t-il ?
			4. Tester la commande `ping -c 5 -t 10 8.8.8.8`. Que se passe-t-il ?
			
	=== "Réponses"
		A venir !
		
??? tips "Fixer le TTL"
	L'option `-t` pour la commande `ping`, sous Linux, permet de fixer un nombre maximum de **hops** possibles. Si la destination est plus lointaine que ce nombre, on aura alors l'erreur `Time to live exceeded`.
	Cette possibilité existe aussi sous windows mais :
	* l'option `-t` désactive poar défaut la limite de 4 paquets `ICMP`, et envoie donc en continu (comme la commande de base sous Linux) ;
	* l'option `-c` fixe le nombre maximal de **hops**, mais nécessite d'être dans une console en mode administrateur pour être utilisée.
	
### La commande `tracert` (ou `traceroute` sous linux)
		
Il est possible de globalement connaître les différents routeurs par lesquels passe un paquet IP, en utilisant le principe précédent :

* on envoie un paquet avec un `TTL` de 1, le premier routeur atteint va décrémenter et atteindre 0, il va donc envoyer un message signalant qu'il a détruit le paquet en question, et dans ce message il y aura bien entendu son adresse IP.
* On fait de même avec un `TTL` de 2, le premier routeur décrémente le `TTL`, le second le décrémente encore une fois, et comme il atteint 0, il détruit le paquet et renvoie un message d'erreur, avec bien entendu son adresse IP.
* On continue ainsi en augmentant le `TTL`.

La commande permettant d'appliquer cette méthode est `tracert` sous windows (`traceroute`sous Linux) :

![Tracert.png](Tracert.png){: style="width:60%; margin:auto;display:block;background-color: #546d78;"}

On constate ici qu'on a bien un passage par 8 machines (7 routeurs plus mon propre PC) :

* le premier routeur d'ip `192.168.1.254` (adresse classique des passerelles chez Free, c'est-à-dire de ma box);
* le second `194.149.164.68`, qui correspond à un routeur Free  (on peut le vérifier avec l'outil [who is](https://www.crawl-tools.com/fr/whois-client/){target = '_blank'};
* etc... jusqu'à atteindre le DNS Google d'ip `8.8.8.8`

!!! question "Tester la commande"

	=== "Enoncé"
	
		1. Depuis l'invite de commande windows (non-testé depuis le lycée... On pourrait avoir des surprises...) :
			1. Tester la commande `tracert 8.8.8.8`.
			2. Tester la commande `tracert 95.142.174.138`
			3. Tester la commande `tracert www.toutatice.fr`. Que se passe-t-il ?
		2. Depuis l'invite de commande Linux de [JupyterHub](https://zonensi.fr:8443){: target="_blank"} :
			1. Tester la commande `traceroute 8.8.8.8`.
			2. Tester la commande `traceroute 95.142.174.138`
			3. Tester la commande `traceroute www.toutatice.fr`. Que se passe-t-il ?

## Routage des paquets deans un réseau

### Routage et topologie de réseau

### Protocoles de routages

## Routage RIP à  vecteur de distance

## Routage OSPF

