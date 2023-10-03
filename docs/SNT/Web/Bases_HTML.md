# Construire une page Web : Bases de HTML

## Une page web ?

!!! question "Découvrir HTML"

    1. Dans le lecteur réseau de votre classe, dossier `Documents en consultation/SNT/Web`, récupérez le fichier `Micro_Maqueen` et copiez-le dans votre répertoire `SNT` dans lequel vous aurez au préalable créé un dossier `web`.

    2. Double-cliquez sur ce fichier. Quel logiciel l'ouvre ?

    3. Quelle est la nature du contenu du fichier ?

    4. Vous pouvez fermer le logiciel. Nous allons changer l'extension du fichier `Micro_Maqueen`. Pour ce faire :

        1. Placez-vous dans votre dossier `SNT/web` à l'aide de votre explorateur de fichier, puis cliquez sur le menu en haut `Affichage`, puis cochez la case `Extensions de noms de fichiers`. Quelle extension a pour l'instant le fichier `Micro_Maqueen` ?

        2.  Sélectionnez le fichier puis appuyez sur `F2` pour renommer, puis changez l'extension `.txt` en `.html`. Que se passe-t-il pour l'icône de fichier ?

    5.  Double-cliquez sur le fichier. Quel logiciel l'ouvre ?

    6.  Quelle est la nature du contenu du fichier ?

    7.  Quelle est l'URL de la page ?

    8.  Dans le dossier `Documents en consultation/SNT/Web`, récupérez les fichiers images `BBC_Microbit.jpg` et `Maqueen.png`, et copiez-les dans le même répertoire que votre fichier `Micro_Maqueen.html`. Rechargez la page web.

        Quels sont les changements apportés ?

    9.  Réduisez sans fermer votre navigateur, puis cliquez-droit sur le fichier `Micro_Maqueen.html`, et sélectionnez `Edit with Notepad++`. Que retrouvez-vous ?

    10. Quelles différences constatez-vous entre le fichier ouvert dans un navigateur, et le fichier ouvert par `Notepad++`?

## Le fond : du texte et de l'hypertexte - HTML


!!! info "HTML et notion de balises"
    Une page web, c'est un fichier contenant du texte, ce texte étant enrichi par un système de {==**balises**==} *ouvrantes* - par exemple `<p>` et *fermantes* - par exemple `</p>`, permettant de **donner un sens particulier au texte encadré par ces balises**.

    Ces balises sont interprétées par le navigateur web et donnent une **sémantique** particulière au texte (titre, paragraphe, élément de liste, etc), ou bien introduisent des comportement particuliers à certains éléments ( transforment en lien hypertextuels, insèrent des images, etc).

    Le langage utilisé qui contient le texte et les balises s'appelle {==**HTML**==} ( d'où le nom de l'extension `.html` ) , qui est un acronyme pour {==**Hyper Text Markup Language**==}, soit *langage de balisage hypertexte*. Il est à noter que `HTML` **n'est pas un langage de programmation**, mais simplement un langage de mise en valeur du texte, privilégiant la mise en avant du sens avant la forme.

    Il existe de nombreux langages de balisages, permettant de donner une forme particulière à du texte ou à des chaines de caractères. Par exemple, `HTML` pour le Web, `LaTeX` pour les documents scientifiques et les formules mathématiques, `XML` pour organiser des données, ou même `Mardown`, un langage ultra simplifié utilisé par exemple dans des Notebooks Jupyter ( que nous utiliserons plus tard dans l'année ), mais aussi sur des plateforme de réseaux sociaux telles que `Discord`.

L'objectif des questions suivantes est de vous faire comprendre le rôle
des balises HTML. Vous devez donc comparer les deux visions du fichier
HTML, celle vue par le navigateur et celle vue par l'éditeur de texte.

!!! question "Ex1 : Comprendre HTML : une balise - vocabulaire"

    Prenons la deuxième ligne du fichier, vue dans `Notepad++`. Celle ci contient une {==**balise ouvrante**==} de **nom** `html`, et d'**attribut** `lang`, encadrés par des **chevrons** `<` et `>`.

    1.  L'attribut `lang` possède une valeur. Quelle est-elle ?

    2.  {==**Toute balise ouvrante doit être fermée**==}. Où se trouve la balise fermante correspondant à `<html lang="fr">` ? Avec quoi la distingue-t-on ?

!!! question  "Ex2 : Comprendre HTML : les principales balises "

    Pour chacun des cas ci-dessous, trouver le couple de balise qui correspond :

    1.  Texte affiché dans l'onglet :

    2.  Titre principal :

    3.  Sous-titre :

    4.  Sous-sous-titre :

    5.  Paragraphe :

    6.  Mise en gras dans un paragraphe :

    7.  Hyperlien :

    8.  Élément d'une liste :

    9.  Liste numérotée :

    10.  Liste à puces :

    11. En-tête de la page :

    12. Corps principal de la page :

    13. Haut du corps de page :

    14. Pied du corps page :

    15. Ensemble du code html :

!!! question "Ex3 : Comprendre HTML - Des balises spécifiques"

    3.  1.  Concernant les balises de **liens hypertextes** de la page, les deux ne se comportent pas de la même manière. Comment expliquer cela ?

        2.  Toujours concernant les liens hypertextes, que doit-on renseigner pour donner la **cible du lien** ?

    4.  1.  Nous n'avons pas évoqué les **images** présentes sur la page. Quelle balise permet d'afficher ces images ? Qu'a-t-elle de particulier par rapport à toutes celles vues avant ?

            !!! warning "Obtenir le lien réel d'une image sur le web"

                Lorsque vous faites une recherche par Google Image ou tout autre moteur de recherche, et que vous cliquez-droit sur une image puis sur `Copier le lien de l'image`, vous **n'obtenez pas le réel lien hypertexte** de l'image, mais un lien crée par le moteur de recherche vers une copie de cette image qu'il stocke dans sur ses serveurs de **manière temporaire**.

                Pour éviter de perdre ainsi l'image, il est toujours préférable d'aller directement sur le site où se situe l'image et de copier le lien correspondant.

        2.  Faites survoler ces deux images par votre pointeur de souris dans votre navigateur. Vous devez constater une différence de traitement entre les deux. Comment l'expliquer ?

        3.  Mais, au départ, avant de copier les fichiers images dans le même répertoire que le fichier `N3_Micro_Maqueen.html`, les images n'étaient pas affichées. Par quoi étaient elles remplacées ?

    5.  Le pied de page est particulier, car il a un caractère spécial. Comment ce caractère est-il représenté en HTML ?

    6.  Il y a trois vidéos, toutes issues de `Youtube` :

        1.  Quelle balise permet de les visionner ? Est-elle fermante ?

        2.  Quels sont les attributs donnés, et à quoi correspondent-ils ?

        3.  L'une de ces vidéos n'a pas le même comportement que les deux
            autres. Comment expliquer cela ?

        !!! tips "Trouver le code pour insérer une vidéo"
            Quand vous visionnez une vidéo sur `Youtube`, sous la vidéo vous avez un icône `Partager`. En cliquant sur cet icône, vous obtenez des liens pour partager sur `Facebook`, `Twitter`, etc. Mais vous avez aussi un icône `Intégrer`. En cliquant sur celui-ci, vous obtenez la balise complète vous permettant d'intégrer la vidéo en question dans votre site web.

    7.  Au milieu du code est inséré ce qu'on appelle un commentaire, c'est-à-dire une ligne qui ne peut être lue que par ceux qui regardent le code source (le contenu réel du HTML). Cette ligne sert à faire des commentaires à la personne qui voudra comprendre le code donné. Quelle balise introduit ces commentaires ?

## À vous de jouer

Vous devez créer une page web sur le {==**sujet de votre choix**==}, contenant :

* un titre principal ;
* deux sous-parties ;
* deux hyperliens vers des sites externes ;
* une liste (à puce ou numérotée) ;
* au moins deux images ;
* une vidéo (ou un lien vers une vidéo).

On respectera aussi les recommandations suivantes :

* Un soin particulier sera apporté à l'orthographe.
* Le copié-collé depuis un autre site doit impérativement mentionner l'origine du texte. Sans ces sources citées, vous pourriez être accusé de plagiat.
* De même l'origine des images ou des vidéos doit être explicitement donné dans le site, soit sous la forme d'infobulles, soit sous la forme d'un commentaire d'image (balises `<figure>` et `<figcaption>`, voir [ici](https://developer.mozilla.org/fr/docs/Web/HTML/Element/figcaption){: target="_blank"}).
* Attention aux informations que vous trouvez sur le web. Certaines sont fortement datées et utilisent des balises qui sont **obsolètes** (comme les balises `<center>`, `<S>`, `<U>`, `<B>`). De manière générale, {==**n'essayez pas de faire de la mise en page !**==} `HTML` n'est pas fait pour ça, nous utiliserons un autre langage pour améliorer notre page.
* La méthode la plus sûre si vous cherchez de nouvelles balises, ou bien des attributs spécifiques, est d'aller sur le site consacré au `HTML` de la [fondation Mozilla](https://developer.mozilla.org/fr/docs/Web/HTML){: target = "_blank"}.

!!! question "Transmettre le/les fichiers"
    Le fichier `.html` de votre site devra être déposé sur pronote à la date indiquée par le professeur.

    Si votre site utilise plusieurs fichiers `HTML` ou des images téléchargées, vous devrez alors créer un fichier compressé (`.zip`) contenant à la fois votre/vos fichier(s) `HTML` et vos images en suivant la méthode ci-dessous :

    * Sélectionnez votre/vos fichier(s) `HTML` ainsi que les fichiers images nécessaires (à l'aide de la touche ++CTRL++ pour faire une sélection multiple).
    * Cliquez droit sur un des fichiers sélectionné puis dans le menu contextuel `7zip`, sélectionnez `Ajouter à XXXX.zip`, où `XXXX` est le nom du dossier dans lequel vous avez vos fichiers. Vous obtiendrez alors un {==**fichier archive**==} qui sera celui que vous transmettrez au professeur.
