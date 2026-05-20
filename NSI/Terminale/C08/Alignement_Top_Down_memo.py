def align_seq_rec(a : str, b : str) :
    if len(a) == 0 and len(b) == 0 :
        return ("","", 0)
    elif len(a) == 0 : 
        return ("", b, len(b))
    elif len(b) == 0 :
        return (a, "", len(a))
    elif a[0] == b[0] :
        S = align_seq_rec(a[1:], b[1:])
        return (a[0]+S[0], b[0]+S[1], S[2])
    else :
        S1 = align_seq_rec(a, b[1:])
        S2 = align_seq_rec(a[1:], b)
        if S1[2]<=S2[2] :
            return ("-"+S1[0], b[0]+S1[1], 1+S1[2])
        else :
            return (a[0]+S2[0], "-"+S2[1], 1+S2[2])
        
        
def align_seq_rec_memo(a : str, b : str) :
    def compute(a : str, b: str, memo : dict) -> tuple:
        if (a,b) in memo :
            return memo[(a,b)]
        if len(a) == 0 and len(b) == 0 :
            memo[(a,b)] = ("","", 0)
            return ("","", 0)
        elif len(a) == 0 :
            memo[(a,b)] = ("", b, len(b))
            return ("", b, len(b))
        elif len(b) == 0 :
            memo[(a,b)] = (a, "", len(a))
            return (a, "", len(a))
        elif a[0] == b[0] :
            S = compute(a[1:], b[1:], memo)
            memo[(a,b)] = (a[0]+S[0], b[0]+S[1], S[2])
            return (a[0]+S[0], b[0]+S[1], S[2])
        else :
            S1 = compute(a, b[1:], memo)
            S2 = compute(a[1:], b, memo)
            if S1[2]<=S2[2] :
                memo[(a,b)] = ("-"+S1[0], b[0]+S1[1], 1+S1[2])
                return ("-"+S1[0], b[0]+S1[1], 1+S1[2])
            else :
                memo[(a,b)] = (a[0]+S2[0], "-"+S2[1], 1+S2[2])
                return (a[0]+S2[0], "-"+S2[1], 1+S2[2])
    
    memo = dict()
    
    
    
    return compute(a,b,memo)
        
        
if __name__ == "__main__" :
    print(align_seq_rec_memo('GRAS', 'GERS')  )
    import time
    
    X = "TTCACCAGAAAAGAACACGGTAGTTACGAGTCCAATATTGTTAAACCG"
    Y = "TTCACGAAAAAGTAACGGGCCGATCTCCAATAAGTGCGACCGAG"
    for i in range(1,min(len(X), len(Y))) :
        
        start = time.time()
        print(align_seq_rec(X[:i], Y[:i]))
        print(f"----> Sans mémoization : {time.time() - start}") 
        start = time.time()
        print(align_seq_rec_memo(X[:i], Y[:i]))
        print(f"----> Avec mémoization : {time.time() - start}") 
        