def bad_fibo(n, memo = dict()) :
    print(f"***** Appel de bad_fibo({n}) avec id de memo {id(memo)} ")    
    if n in memo :
        print(f"=> Déjà calculé !")    
        return memo[n]
    elif n <= 1 :
        print(f"=> Premier appel de bad_fibo({n})")
        memo[n] = 1
        return memo[n]
    else :
        print(f"=> Premier appel de bad_fibo({n})")
        memo[n] = bad_fibo(n-1, memo)+bad_fibo(n-2, memo)
        return memo[n]

print("Première exécution")
print(bad_fibo(5))
print("\n"*3)
print("Deuxième exécution")
print(bad_fibo(6))