def fibonacci(n : int ) -> int :
    if  n ==0 or n == 1 :
        return 1
    else :
        return fibonacci(n-1)+fibonacci(n-2)
    
if __name__ == "__main__" :
    print(fibonacci(5))