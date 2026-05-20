def recherche(mot :str, chaine:str) -> bool :
    lmot = len(mot)
    lchaine = len(chaine)
    i = 0
    while i< lchaine-lmot+1 :
        trouve = True
        j = 0
        while trouve and  j< lmot :
            if mot[j] != chaine[i+j] :
                trouve = False
            j += 1 
        if trouve :
            return True
        i += 1
    return False

def lit_texte(fichier) :
    with open(fichier, 'r', encoding='utf8') as f :
        contenu = f.readlines()
    return " ".join(contenu).replace("\n", "")
                
phrase = "Mais toutes ces pensées ne durèrent "\
"que l'espace d'une seconde, le temps qu'il portât "\
"la main à son coeur, reprît sa respiration et parvint "\
"à sourire pour dissimuler sa torture. Déjà il recommençait "\
"à poser ses questions. Car sa jalousie qui avait pris une peine "\
"qu'un ennemi ne se serait pas donnée pour arriver à lui faire "\
"asséner ce coup, à lui faire faire la connaissance de la douleur "\
"la plus cruelle qu'il n'eût encore jamais connue, sa jalousie ne "\
"trouvait pas qu'il eut assez souffert et cherchait à lui faire recevoir "\
"une blessure plus profond encore."