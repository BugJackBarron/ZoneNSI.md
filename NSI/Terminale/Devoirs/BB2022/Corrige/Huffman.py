from graphviz import Digraph


class Noeud:
    def __init__(self, poids, caractere=None, gauche=None,droit=None):
        self.poids = poids
        self.caractere = caractere
        self.gauche = gauche
        self.droit = droit

    def est_feuille(self):
        """Renvoie True si l’arbre est une feuille, False sinon."""
        return self.gauche is None and self.droit is None
    


def fusionner(G, D) :
    return Noeud(G.poids+D.poids, gauche=G, droit = D)

def get_dict(chaine) :
    
    carac = set([c for c in chaine])
    return {c:chaine.count(c) for c in carac}

def construire_liste_arbres(d) :
    return [Noeud(v, caractere=k) for k,v in d.items()]

def construire_arbre_huffman(d):
    liste_arbres = construire_liste_arbres(d) 
    while len(liste_arbres) > 1: 
        G = extraire_arbre_poids_min(liste_arbres)
        D = extraire_arbre_poids_min(liste_arbres)
        T = fusionner(G, D)
        liste_arbres.append(T)
    return T

def extraire_arbre_poids_min ( liste_arbres ):
    poids_mini = liste_arbres[0]. poids
    indice_mini = 0
    for i in range(len(liste_arbres)) :
        if liste_arbres[i].poids< poids_mini :
            poids_mini = liste_arbres[i].poids
            indice_mini = i
    arbre_extrait = liste_arbres.pop( indice_mini )
    return arbre_extrait

def construire_codes (A, chemin, dico ):
    if A.est_feuille() :
        dico [A.caractere ] = chemin
    else :
        construire_codes (A.gauche, chemin + "0", dico)
        construire_codes (A.droit , chemin + "1", dico)


def trace_graph(G) :
    dot = Digraph('Huffman',format='png', graph_attr={'rankdir': 'BT'})
    file = [(G, None)]
    num = -1
    while file != [] :
        node, parent = file.pop()
        num += 1
        txt = f"{node.poids}" if node.caractere is None else f"{node.caractere} | {node.poids}"
        dot.node(str(num), txt)
        if node.gauche is not None :
            file.append((node.gauche, num))
        if node.droit is not None :
            file.append((node.droit, num))
        
        if parent != None :
            dot.edge(str(num), str(parent))
    dot.render(directory='', view=True)
    
    
    
if __name__ == "__main__" :
    phrase = """
Et aussitôt prenant ses jambes à son cou, il s'enfuit dans la
direction du camp, avec la vitesse des gens de son pays si
renommés pour leur agilité; mais, quelle que fût la rapidité de sa
course, le premier qui avait tiré, ayant eu le temps de recharger
son arme, lui tira un second coup si bien ajusté, cette fois, que
la balle traversa son feutre et le fit voler à dix pas de lui.

Cependant, comme d'Artagnan n'avait pas d'autre chapeau, il
ramassa le sien tout en courant, arriva fort essoufflé et fort
pâle, dans son logis, s'assit sans rien dire à personne et se mit
à réfléchir.

Cet événement pouvait avoir trois causes:

La première et la plus naturelle pouvait être une embuscade des
Rochelois, qui n'eussent pas été fâchés de tuer un des gardes de
Sa Majesté, d'abord parce que c'était un ennemi de moins, et que
cet ennemi pouvait avoir une bourse bien garnie dans sa poche.

D'Artagnan prit son chapeau, examina le trou de la balle, et
secoua la tête. La balle n'était pas une balle de mousquet,
c'était une balle d'arquebuse; la justesse du coup lui avait déjà
donné l'idée qu'il avait été tiré par une arme particulière: ce
n'était donc pas une embuscade militaire, puisque la balle n'était
pas de calibre.

Ce pouvait être un bon souvenir de M. le cardinal. On se rappelle
qu'au moment même où il avait, grâce à ce bienheureux rayon de
soleil, aperçu le canon du fusil, il s'étonnait de la longanimité
de Son Éminence à son égard.

Mais d'Artagnan secoua la tête. Pour les gens vers lesquels elle
n'avait qu'à étendre la main, Son Éminence recourait rarement à de
pareils moyens.

Ce pouvait être une vengeance de Milady.

Ceci, c'était plus probable.

Il chercha inutilement à se rappeler ou les traits ou le costume
des assassins; il s'était éloigné d'eux si rapidement, qu'il
n'avait eu le loisir de rien remarquer.

«Ah! mes pauvres amis, murmura d'Artagnan, où êtes-vous? et que
vous me faites faute!»

D'Artagnan passa une fort mauvaise nuit. Trois ou quatre fois il
se réveilla en sursaut, se figurant qu'un homme s'approchait de
son lit pour le poignarder. Cependant le jour parut sans que
l'obscurité eût amené aucun incident.

Mais d'Artagnan se douta bien que ce qui était différé n'était pas
perdu.

D'Artagnan resta toute la journée dans son logis; il se donna pour
excuse, vis-à-vis de lui-même, que le temps était mauvais.

Le surlendemain, à neuf heures, on battit aux champs. Le duc
d'Orléans visitait les postes. Les gardes coururent aux armes,
d'Artagnan prit son rang au milieu de ses camarades.

Monsieur passa sur le front de bataille; puis tous les officiers
supérieurs s'approchèrent de lui pour lui faire leur cour, M. des
Essarts, le capitaine des gardes, comme les autres.

Au bout d'un instant il parut à d'Artagnan que M. des Essarts lui
faisait signe de s'approcher de lui: il attendit un nouveau geste
de son supérieur, craignant de se tromper, mais ce geste s'étant
renouvelé, il quitta les rangs et s'avança pour prendre l'ordre.

«Monsieur va demander des hommes de bonne volonté pour une mission
dangereuse, mais qui fera honneur à ceux qui l'auront accomplie,
et je vous ai fait signe afin que vous vous tinssiez prêt.

-- Merci, mon capitaine!» répondit d'Artagnan, qui ne demandait
pas mieux que de se distinguer sous les yeux du lieutenant
général.

En effet, les Rochelois avaient fait une sortie pendant la nuit et
avaient repris un bastion dont l'armée royaliste s'était emparée
deux jours auparavant; il s'agissait de pousser une reconnaissance
perdue pour voir comment l'armée gardait ce bastion.

Effectivement, au bout de quelques instants, Monsieur éleva la
voix et dit:

«Il me faudrait, pour cette mission, trois ou quatre volontaires
conduits par un homme sûr.

-- Quant à l'homme sûr, je l'ai sous la main, Monseigneur, dit
M. des Essarts en montrant d'Artagnan; et quant aux quatre ou cinq
volontaires, Monseigneur n'a qu'à faire connaître ses intentions,
et les hommes ne lui manqueront pas.

-- Quatre hommes de bonne volonté pour venir se faire tuer avec
moi!» dit d'Artagnan en levant son épée.

Deux de ses camarades aux gardes s'élancèrent aussitôt, et deux
soldats s'étant joints à eux, il se trouva que le nombre demandé
était suffisant; d'Artagnan refusa donc tous les autres, ne
voulant pas faire de passe-droit à ceux qui avaient la priorité.

On ignorait si, après la prise du bastion, les Rochelois l'avaient
évacué ou s'ils y avaient laissé garnison; il fallait donc
examiner le lieu indiqué d'assez près pour vérifier la chose.
"""
    occurences = get_dict(phrase.replace("\n", ""))
    huffman = construire_arbre_huffman(occurences)
    #trace_graph(huffman)
    converter = dict()
    construire_codes(huffman,"", converter)
    compressed = "".join(converter[l] for l in phrase if l!= "\n")
    print(f"Phrase compressée : {compressed}")
    print(f"Compression : {len(compressed)}/{8*(len(phrase)-2)} = {len(compressed)/(8*(len(phrase)-2))}")