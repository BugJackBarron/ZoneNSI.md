#!/usr/bin/env python 
#-*- coding: utf-8 -*-

import time
from random import randint
import matplotlib.pyplot as plt
import pickle

def make_obj_sub_list_from_list_and_int(obj_list : list, nb : int) :
    i = 0
    return_list = []
    while nb != 0 :
        if nb%2 == 1 :
            return_list.append(obj_list[i])
        i += 1
        nb = nb//2
    return return_list
                
def sacADosNaif(listeObj : dict, masseMax : int) -> list :
    """ Calcule la solution optimale pour le problème du sac à dos"""
    optimale = []
    valeurOptimale = 0
    n = len(listeObj)
    for nb in range(2**n) :
        se = make_obj_sub_list_from_list_and_int(list(listeObj.keys()), nb)
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
        "B" : {'masse' : 7, 'valeur' : 400},
        "C" : {'masse' : 8, 'valeur' : 300},
        "D" : {'masse' : 10, 'valeur' : 300},
                }
    print(sacADosNaif(objets,30))
#     NREP = 20
#     ntT = [0]*NREP
#     gtT = [0]*NREP
#     vnT = [ [] for _ in range(NREP) ]
#     vgT = [ [] for _ in range(NREP) ]
#     LISSAGE  = 3
#     for i in range(LISSAGE) :
#         nt,gt, vn, vg = compare(NREP)
#         for i in range(NREP) :
#             vnT[i].append(vn)
#             vgT[i].append(vg)
#             ntT[i]+=nt[i]
#             gtT[i] += gt[i]
#     gt = [t/LISSAGE for t in gtT]
#     nt = [t/LISSAGE for t in ntT]
#     with open('compareGreedyNatural.dat','wb') as file :
#         pickle.dump((nt,gt, vnT, vgT), file) 
    