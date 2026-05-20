def fibo(n, cnt) :   
    if n == 0 :
        cnt[0] += 0
        return  0
    elif n == 1 :
        cnt[1] += 1
        return 1
    else :
        cnt[n-1] += 1
        cnt[n-2] += 1
        return fibo(n-1, cnt) + fibo(n-2, cnt)
    
    
def fiboAsc(n) :
    F = [0]*(n+1)
    F[1] = 1
    for i in range(2,n+1) :
        F[i] = F[i-1] + F[i-2]
    return F[n]

def fiboDesc(n) :

    memo = [0, 1]+[None]*(n-1)
    
    def compute(n, memo) :
        if memo[n] is  None :
            memo[n] = compute(n-1, memo) + compute(n-2, memo)
        return memo[n]
        
    return compute(n, memo)


