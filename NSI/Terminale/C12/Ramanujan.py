

def fact(n) :
    if n == 0:
        return 1
    return n*fact(n-1)


def ramanujan(n) :
    ram1 = 2*2**(1/2)/9801
    ram2=0
    for k in range(n) :
        ram2 += fact(4*k)*(1103+26390*k)/(fact(k)**4*396**(4*k))
        print(f"{k} => ram = {ram1*ram2} => 1/ram = {1/(ram1*ram2)}") 