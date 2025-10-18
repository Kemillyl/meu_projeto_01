a= float(input('qual é o valor desse produto?R$'))
b= (a * 5/100)
c= a - b
print('com o desconto o seu item fica R${:.2f}'.format(c))
#também posso fazer uma variavel que fique a-(a * 5 / 100)