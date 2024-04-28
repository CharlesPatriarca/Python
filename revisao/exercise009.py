cont = 0
soma = 0

for x in range (4):
    num = int(input(f'Digite o número {cont+1}: '))
    soma = num + soma
    cont += 1

media = soma / 4

print (f' A soma é {soma} e a média é {media}')