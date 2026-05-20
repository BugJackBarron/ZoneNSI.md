import secondDegre_v1 as sD

p = input("Donnez les coefficients du polynome séparés par des virgules :")

p = tuple(map(float, p.split(",")))

p = sD.polynome(p)

print(sD.tangente(p,3))
