k = (float(input('quantos km foram percorridos:')))
d = (int(input('quantos dias voce utilizou o carro?')))
calculo = (0.15 * k) + (60 * d)
print('o preço a pagar será de R$ {:.2f}'.format(calculo))