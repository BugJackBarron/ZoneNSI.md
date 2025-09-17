def tabValeurMassique(L : dict)  ->list :
    tab =[]
    for k, v in L.items() :
        tab.append((k, v[1]/v[0]))
    return sorted(tab, key = lambda x : x[1], reverse = True)


def sacADos(L, masseMaxi = 30 ) :
    vmTriee = tabValeurMassique(L)
    dansLeSac= []
    masseTotale = 0
    i = 0
    objetPris = vmTriee[i]
    nomObjet = objetPris[0]
    masseObjet = L[nomObjet][0]
    while masseTotale + masseObjet <= masseMaxi :
        dansLeSac.append(nomObjet)
        masseTotale +=masseObjet
        i+=1
        objetPris = vmTriee[i]
        nomObjet = objetPris[0]
        masseObjet = L[nomObjet][0]
    return dansLeSac


if __name__ == "__main__" :
    listeObjets = {
        "A" : (13, 700),
        "B" : (12, 400),
        "C" : (8, 300),
        "D" : (10, 300)
        }
    
                   
                   