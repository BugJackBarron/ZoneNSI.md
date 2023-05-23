def supprime_accent(ligne):
    """ supprime les accents du texte source """
    accents = { 'a': ['à', 'ã', 'á', 'â'],
                'e': ['é', 'è', 'ê', 'ë'],
                'i': ['î', 'ï'],
                'u': ['ù', 'ü', 'û'],
                'o': ['ô', 'ö'] }
    for (char, accented_chars) in accents.items():
        for accented_char in accented_chars:
            ligne = ligne.replace(accented_char, char)
    return ligne

def formate_texte(texte : str) -> str :
    texte_formate = ""
    for letter in texte.lower() :
        if letter in 'àâä' :
            texte_formate +='a'
        elif letter in 'éèêë' :
            texte_formate += 'e'
        elif letter in 'îïì' :
            texte_formate += 'i'
        elif letter in 'ôöò' :
            texte_formate += 'o'
        elif letter in 'üûù' :
            texte_formate +='u'
        elif 97<= ord(letter) <= 122 :
            texte_formate += letter.lower()
    return texte_formate

def code_Cesar(texte :str, cle : int) -> str :
    chiffre = ""
    for letter in formate_texte(texte).upper() :
        if 65<=ord(letter.upper())<=90 :
            chiffre += chr(((ord(letter)-65)+cle)%26+65)
    return chiffre

def brute_force_Cesar(texte : str) -> str :
    decrypte = []
    for k in range(1,26) :
        decrypte.append(code_Cesar(texte, k))
    return decrypte

def get_freq_texte(texte : str) -> dict :
    dico = dict()
    for letter in texte :
        if letter in dico :
            dico[letter] += 1
        else :
            dico[letter] = 1
    return dico

def attaque_Cesar_analyse_frequence(texte : str) -> str:
    dico = get_freq_texte(texte)
    max_dico = []
    maxi = 0
    for letter in dico :
        if dico[letter]> maxi :
            max_dico=[letter]
            maxi = dico[letter]
        elif dico[letter] == maxi :
            max_dico.append(letter)
    possible_keys = [ord(k)-ord('E') for k in max_dico]
    possible_texts = [ f"Clé {k} :\n\n"+code_Cesar(crypto, 26-k) for k in possible_keys]
    return possible_texts
    
def get_unicode(chaine : str) -> list :
    uni = []
    for l in chaine :
        uni.append(ord(l))
    return uni

def get_string(liste : list) -> str :
    return "".join([chr(l) for l in liste])

def chiffre_XOR(texte : list, cle : list) -> list :
    chiffre = []
    for i in range(len(texte)) :
        chiffre.append(texte[i]^cle[i%len(cle)])
    return chiffre

def all_possible(length : int) :
    if length ==0 :
        return ['']
    poss = []
    disp = all_possible(length-1)
    for uni in range(65, 65+26) :
        for d in disp :
            poss.append(chr(uni)+d)
    return poss
                     
def cryptanalyse_XOR(chiffre : list, start : str, taille_cle : int) :
    poss_keys = []
    for k in all_possible(taille_cle) :
        decode = get_string(chiffre_XOR(chiffre, get_unicode(k)))
        if decode.startswith(start) :
            poss_keys.append(k)
    return poss_keys
        
                      
            
 

if __name__ == "__main__" :
    txt = """Pendant les quelques instants qu'il venait d'entrevoir Phileas Fogg,
Passepartout avait rapidement, mais soigneusement examiné son futur
maître. C'était un homme qui pouvait avoir quarante ans, de figure noble
et belle, haut de taille, que ne déparait pas un léger embonpoint, blond
de cheveux et de favoris, front uni sans apparences de rides aux tempes,
figure plutôt pâle que colorée, dents magnifiques. Il paraissait
posséder au plus haut degré ce que les physionomistes appellent «le
repos dans l'action», faculté commune à tous ceux qui font plus de
besogne que de bruit. Calme, flegmatique, l'oeil pur, la paupière
immobile, c'était le type achevé de ces Anglais à sang-froid qui se
rencontrent assez fréquemment dans le Royaume-Uni, et dont Angelica
Kauffmann a merveilleusement rendu sous son pinceau l'attitude un peu
académique. Vu dans les divers actes de son existence, ce gentleman
donnait l'idée d'un être bien équilibré dans toutes ses parties,
justement pondéré, aussi parfait qu'un chronomètre de Leroy ou de
Earnshaw. C'est qu'en effet, Phileas Fogg était l'exactitude
personnifiée, ce qui se voyait clairement à «l'expression de ses pieds
et de ses mains», car chez l'homme, aussi bien que chez les animaux, les
membres eux-mêmes sont des organes expressifs des passions.

Phileas Fogg était de ces gens mathématiquement exacts, qui, jamais
pressés et toujours prêts, sont économes de leurs pas et de leurs
mouvements. Il ne faisait pas une enjambée de trop, allant toujours par
le plus court. Il ne perdait pas un regard au plafond. Il ne se
permettait aucun geste superflu. On ne l'avait jamais vu ému ni troublé.
C'était l'homme le moins hâté du monde, mais il arrivait toujours à
temps. Toutefois, on comprendra qu'il vécût seul et pour ainsi dire en
dehors de toute relation sociale. Il savait que dans la vie il faut
faire la part des frottements, et comme les frottements retardent, il ne
se frottait à personne.

Quant à Jean, dit Passepartout, un vrai Parisien de Paris, depuis cinq
ans qu'il habitait l'Angleterre et y faisait à Londres le métier de
valet de chambre, il avait cherché vainement un maître auquel il pût
s'attacher.

Passepartout n'était point un de ces Frontins ou Mascarilles qui, les
épaules hautes, le nez au vent, le regard assuré, l'oeil sec, ne sont
que d'impudents drôles. Non. Passepartout était un brave garçon, de
physionomie aimable, aux lèvres un peu saillantes, toujours prêtes à
goûter ou à caresser, un être doux et serviable, avec une de ces bonnes
têtes rondes que l'on aime à voir sur les épaules d'un ami. Il avait les
yeux bleus, le teint animé, la figure assez grasse pour qu'il pût
lui-même voir les pommettes de ses joues, la poitrine large, la taille
forte, une musculature vigoureuse, et il possédait une force herculéenne
que les exercices de sa jeunesse avaient admirablement développée. Ses
cheveux bruns étaient un peu rageurs. Si les sculpteurs de l'Antiquité
connaissaient dix-huit façons d'arranger la chevelure de Minerve,
Passepartout n'en connaissait qu'une pour disposer la sienne: trois
coups de démêloir, et il était coiffé.

De dire si le caractère expansif de ce garçon s'accorderait avec celui
de Phileas Fogg, c'est ce que la prudence la plus élémentaire ne permet
pas. Passepartout serait-il ce domestique foncièrement exact qu'il
fallait à son maître? On ne le verrait qu'à l'user. Après avoir eu, on
le sait, une jeunesse assez vagabonde, il aspirait au repos. Ayant
entendu vanter le méthodisme anglais et la froideur proverbiale des
gentlemen, il vint chercher fortune en Angleterre. Mais, jusqu'alors, le
sort l'avait mal servi. Il n'avait pu prendre racine nulle part. Il
avait fait dix maisons. Dans toutes, on était fantasque, inégal, coureur
d'aventures ou coureur de pays,--ce qui ne pouvait plus convenir à
Passepartout. Son dernier maître, le jeune Lord Longsferry, membre du
Parlement, après avoir passé ses nuits dans les «oysters-rooms»
d'Hay-Market, rentrait trop souvent au logis sur les épaules des
policemen. Passepartout, voulant avant tout pouvoir respecter son
maître, risqua quelques respectueuses observations qui furent mal
reçues, et il rompit. Il apprit, sur les entrefaites, que Phileas Fogg,
esq., cherchait un domestique. Il prit des renseignements sur ce
gentleman. Un personnage dont l'existence était si régulière, qui ne
découchait pas, qui ne voyageait pas, qui ne s'absentait jamais, pas
même un jour, ne pouvait que lui convenir. Il se présenta et fut admis
dans les circonstances que l'on sait.

Passepartout--onze heures et demie étant sonnées--se trouvait donc seul
dans la maison de Saville-row. Aussitôt il en commença l'inspection. Il
la parcourut de la cave au grenier. Cette maison propre, rangée, sévère,
puritaine, bien organisée pour le service, lui plut. Elle lui fit
l'effet d'une belle coquille de colimaçon, mais d'une coquille éclairée
et chauffée au gaz, car l'hydrogène carburé y suffisait à tous les
besoins de lumière et de chaleur. Passepartout trouva sans peine, au
second étage, la chambre qui lui était destinée. Elle lui convint. Des
timbres électriques et des tuyaux acoustiques la mettaient en
communication avec les appartements de l'entresol et du premier étage.
Sur la cheminée, une pendule électrique correspondait avec la pendule de
la chambre à coucher de Phileas Fogg, et les deux appareils battaient au
même instant, la même seconde.

«Cela me va, cela me va!» se dit Passepartout.

Il remarqua aussi, dans sa chambre, une notice affichée au-dessus de la
pendule. C'était le programme du service quotidien. Il
comprenait--depuis huit heures du matin, heure réglementaire à laquelle
se levait Phileas Fogg, jusqu'à onze heures et demie, heure à laquelle
il quittait sa maison pour aller déjeuner au Reform-Club--tous les
détails du service, le thé et les rôties de huit heures vingt-trois,
l'eau pour la barbe de neuf heures trente-sept, la coiffure de dix
heures moins vingt, etc. Puis de onze heures et demie du matin à
minuit--heure à laquelle se couchait le méthodique gentleman--, tout
était noté, prévu, régularisé. Passepartout se fit une joie de méditer
ce programme et d'en graver les divers articles dans son esprit.

Quant à la garde-robe de monsieur, elle était fort bien montée et
merveilleusement comprise. Chaque pantalon, habit ou gilet portait un
numéro d'ordre reproduit sur un registre d'entrée et de sortie,
indiquant la date à laquelle, suivant la saison, ces vêtements devaient
être tour à tour portés. Même réglementation pour les chaussures.

En somme, dans cette maison de Saville-row qui devait être le temple du
désordre à l'époque de l'illustre mais dissipé Sheridan--, ameublement
confortable, annonçant une belle aisance. Pas de bibliothèque, pas de
livres, qui eussent été sans utilité pour Mr. Fogg, puisque le
Reform-Club mettait à sa disposition deux bibliothèques, l'une consacrée
aux lettres, l'autre au droit et à la politique. Dans la chambre à
coucher, un coffre-fort de moyenne grandeur, que sa construction
défendait aussi bien de l'incendie que du vol. Point d'armes dans la
maison, aucun ustensile de chasse ou de guerre. Tout y dénotait les
habitudes les plus pacifiques.
"""
    crypto = code_Cesar(supprime_accent(txt), 19)
    
    
    with open('Petit_Mystere.txt', 'w') as f :
        f.write(crypto)
        
    with open("brute_force_result", "w") as f :
        for i, line in enumerate(brute_force_Cesar(crypto)) :
            f.write(f"Clé {i+1} :\n\n")
            f.write(line)
            f.write("\n\n\n")
            
    with open("Not_Mystere.txt", "r") as f :
        nm = f.read()
        with open('Grand_Mystere.txt', 'w') as f2 :
            f2.write(code_Cesar(formate_texte(nm), 17))