n1 = float(input(f'Digite sua nota: '))
n2 = float(input(f'Digite sua nota: '))
n3 = float(input(f'Digite sua nota: '))

media = (n1 + n2 + n3) // 3
print (media)

if media < 7:
    print ('Reprovado')
else:
    print ('Aprovado')