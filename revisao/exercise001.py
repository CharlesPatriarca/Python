soma = 0

for x in range (2):
    nota = float(input('Digite sua nota: '))
    while nota < 0 or nota > 10:
        nota = float(input('Nota inválida, digite novamente: '))

    soma = soma + nota

media = soma / 2

print (f'Sua média foi: {media}')