import time                                                

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f" {method.__name__} ({args},{kw}) {te-ts}" )
        return result

    return timed


def tri_insertion(tab): 
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k

@timeit
def fusion(t1, t2) :
    tf = [0]*(len(t1)+len(t2))
    i, j = 0, 0
    for k in range(len(tf)) :
        if  i<len(t1) and j<len(t2) :
            if t1[i]<t2[j] :
                tf[k] = t1[i]
                i+=1
            else :
                tf[k] = t2[j]
                j+=1
        elif i<len(t1) :
            tf[k] = t1[i]
            i+=1
        elif  j<t2[j] :
            tf[k] = t2[j]
            j+=1
    return tf