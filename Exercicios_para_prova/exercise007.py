t1 = input('Digite o nome do seu time: ')
g1 = int(input('Quantos gols seu time fez? '))

t2 = input('Digite o nome do seu time: ')
g2 = int(input('Quantos gols seu time fez? '))

if g1 > g2:
    print (f'{t1} venceu')
elif g2 > g1:
    print (f'{t2} venceu')
else:
    print ('empate')
