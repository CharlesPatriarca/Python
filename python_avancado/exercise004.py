notas = [0,0,0,0,0]
soma = 0
cont = 0

# receber notas e guarda no array
for x in range (len(notas)):
    notas[x] = float(input('Digite as notas: '))

# serve para somar todas as notas
for y in range (len(notas)):
    soma = soma + notas[y]
media = soma / 5

for z in range (len(notas)):
    if notas[z] >= media:
        cont = cont + 1
print (f'A média da turma é {media} e {cont} foram aprovados')