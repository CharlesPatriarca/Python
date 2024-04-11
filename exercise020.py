intervalo = 0
noneIntervalo = 0
for hack in range (10):
    numbers = int(input('Digite 10 de novo: '))
    if numbers >= 10 and numbers <= 20:
        intervalo += 1

    else:
        noneIntervalo += 1

print (f'Dentro do intervalo entre 10 e 20 existem {intervalo} números')
print (f'Fora do intervalo existem {noneIntervalo} números')

