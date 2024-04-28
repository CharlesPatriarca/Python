e = 'E'
g = 'G'
etanol = 4.90
gasolina = 5.80

lt = int(input('Quantos litros? '))
comb = input('Qual combustível? ')

tEt = lt * etanol
tGs = lt * gasolina

if comb == e:
    print (tEt)
else:
    print(tGs)