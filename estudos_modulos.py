import math
#funções teóricas de números

resultado = math.comb(5,2) #escolher k itens de n itens sem ordem e repetição
print('combinações possiveis',resultado)

resul1 = math.factorial(5) #fatorial
print('o resultado da fatoração é', resul1)

resul2 = math.gcd(12,18) #máximo divisor comum, maior divisor em comum dos dois números
print('mdc entre 12 e 18',resul2)

result3 = math.isqrt(10) #raiz quadrada, só mostra resultados inteiros.
print('a raiz quadrada de 10 é',result3)

result4 = math.lcm(4,6) #mínimo multiplo comum entre dois ou mais números, o menor número divisor diferente de zero
print('mmc de 4 e 6 é', result4)

result5 = math.perm(5,2) #escolhe k itens de n itens, mas com ordem
print('combinações possíveis com ordem ',result5)

#funções aritméticas de ponto flutuante
print(math.ceil(-10.1))#exibe o número inteiro que está "acima"

result6 = math.fabs(-7) #mostra o valor absoluto da variável
print('o resultado absoluto é',result6)

result7 = math.floor(4.9)#desce o número para o inteiro mais baixo, com negativo o menor é o mais distante de zero
print('o resultado é',result7)

result8 = math.fma (2,3,4) #multiplicação e adição fundida
print('a multiplicação e adição é igual a',result8)

result9 = math.fmod(10,3)#resto da divisão
print('o resto da divisão é',result9)

result10 = math.modf(5.75)#parte fracionária e parte inteira
print('a parte decimal e parte inteira é')

result11 = math.remainder(10,3)
print('o resultado dessa operação é',result11)

result12 = math.trunc (4.99)
print('a parte inteira desse número é',result12)


