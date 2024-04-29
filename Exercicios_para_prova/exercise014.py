anoAtual = 2024
conf = 'S'
idade = int(input('Sua idade: '))
aniv = input('Ja fez anivérsario? ')



if aniv == 'S' or aniv == 's':
    nasc = anoAtual - idade
else:
    nasc = anoAtual - idade - 1
print (f'Você nasceu no ano de {nasc}')