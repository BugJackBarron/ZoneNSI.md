#!/usr/bin/env python 
#-*- coding: utf-8 -*-

import time
from random import randint
import matplotlib.pyplot as plt
import pickle

def makeTree(T : list)  ->list :
    """fonction récursive renvoyant l'ensemble des sous-ensembles non vides d'un ensemble
de départ donné sous la forme d'une liste. L'ensemble de départ doit être non vide"""
    #Cas de base : la liste ne contient qu'un seul élément
    if len(T) == 1 :
        return [T]
    else :
        # Sinon création de la liste des sous-ensembles
        comp = []
        #on créé une copie locale de la liste de départ
        nT = T[:]
        # Pour chaque élément de la liste de départ
        for e in T :
            # On ajoute le singleton correspondant
            comp.append([e])
            #On le supprime de la liste locale
            nT.remove(e)
            # On exécute récursivemment la fonction makeTree
            # sur la liste locale 
            for ne in makeTree(nT) :
                #et pour chaque sous-ensemble obtenu, on rajoute l'élément e
                comp.append([e]+ne)
        return comp
            
def sacADosNaif(listeObj : dict, masseMax : int) -> list :
    """ Calcule la solution optimale pour le problème du sac à dos"""
    optimale = []
    valeurOptimale = 0
    for se in makeTree([ name for name in listeObj.keys()]) :
        masseLocale = sum([listeObj[nom]['masse'] for nom in se])
        valeurLocale = sum([listeObj[nom]['valeur'] for nom in se])
        if valeurLocale >valeurOptimale  and masseLocale<=masseMax :
            valeurOptimale = valeurLocale
            optimale = se
    return optimale, valeurOptimale


#### FONCTIONS NECESSAIRES POUR L'ALGO GLOUTON

def tabValeurMassique(L : dict)  ->list :
    tab =[]
    for k, v in L.items() :
        tab.append((k, v['valeur']/v['masse']))
    return sorted(tab, key = lambda x : x[1], reverse = True)


def sacADosGlouton(L, masseMaxi ) :
    vmTriee = tabValeurMassique(L)
    dansLeSac= []
    masseTotale = 0
    i = 0
    objetPris = vmTriee[i]
    nomObjet = objetPris[0]
    masseObjet = L[nomObjet]['masse']
    while masseTotale + masseObjet <= masseMaxi  and i<len(vmTriee)-1:
        dansLeSac.append(nomObjet)
        masseTotale +=masseObjet
        i+=1
        objetPris = vmTriee[i]
        nomObjet = objetPris[0]
        masseObjet = L[nomObjet]['masse']
    return dansLeSac

### FONCTION DE COMPARAISON ENTRE LES DEUX METHODES
def compare(maxIteration) :
    naifTime = [0]
    gloutonTime = [0]
    for i in range(1,maxIteration) :
        print(f"**************** TEST POUR {i} objets******************")
        objets=dict()
        TAILLE = i
        FACTEUR_TAILLE = 15
        for i in range(TAILLE) :
            objets[i] = {'masse': randint(1,30), 'valeur' : randint(1,15)*100}
        start = time.time()
        what = sacADosNaif(objets, TAILLE*FACTEUR_TAILLE)
        duration = time.time() - start
        naifTime.append(duration)
        valeurNaif = what[-1]
        print(f"**ALGO NAIF ** {what} : {duration}")
        start = time.time()
        what = sacADosGlouton(objets, TAILLE*FACTEUR_TAILLE)
        duration = time.time() - start
        valeurGlouton = sum([objets[e]['valeur'] for e in what])
        gloutonTime.append(duration)
        print(f"**ALGO GLOUTON** {what}, {valeurGlouton}  : {duration} ")
        print()
    return naifTime, gloutonTime, valeurNaif, valeurGlouton


    

if __name__ == "__main__" :
    objets = {
        "A" : {'masse' : 13, 'valeur' : 700},
        "B" : {'masse' : 12, 'valeur' : 400},
        "C" : {'masse' : 8, 'valeur' : 300},
        "D" : {'masse' : 10, 'valeur' : 300},
                }
    print(sacADosNaif(objets,30))
    NREP = 15
    ntT = [0]*NREP
    gtT = [0]*NREP
    vnT = [ [] for _ in range(NREP) ]
    vgT = [ [] for _ in range(NREP) ]
    LISSAGE  = 1
    for i in range(LISSAGE) :
        nt,gt, vn, vg = compare(NREP)
        for i in range(NREP) :
            vnT[i].append(vn)
            vgT[i].append(vg)
            ntT[i]+=nt[i]
            gtT[i] += gt[i]
    gt = [t/LISSAGE for t in gtT]
    nt = [t/LISSAGE for t in ntT]
    with open('compareGreedyNatural.dat','wb') as file :
        pickle.dump((nt,gt, vnT, vgT), file)
    