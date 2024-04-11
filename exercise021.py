soma = 0
divisor = 0
for g in range (3):
    valores = int(input('Digite sua notas: ')) #+ valores
    if valores >= 0 and valores <= 10:
        soma += valores
        divisor += 1

        #media = valores//3
if divisor != 0:
    media = soma / divisor
    print(media)
else:
    print('Reveja sua vida')


