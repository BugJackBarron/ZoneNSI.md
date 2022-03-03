import time

def fibo(n) :
	if n == 0 :
		return 	0
	elif n == 1 :
		return 1
	else :
		return fibo(n-1) + fibo(n-2)

for n in range(100) :
    start = time.perf_counter()
    print(f"fibo({n}) = {fibo(n)}", end="")
    end = time.perf_counter()
    print(f" Temps : {end - start}")
