from math import pow, sqrt
#como eu pensei
co = float(input("Digite o valor do cateto oposto:"))
ca = float(input("Digite o valor do cateto adjacente:"))
hipo = sqrt(pow(co, 2)+pow(ca, 2))
print("O valor da hipotenusa é {:.2f}".format(hipo))

#maneira simplificada de calcular
"""
hipo = math.hipot(co,ca)
ou
sem importação 
hipo=(co**2 + ca**2) **(1/2)
"""