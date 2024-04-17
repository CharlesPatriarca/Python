condicao = 'S'

while condicao == 'S' or condicao == 's' or condicao == 'Sim' or condicao == 'sim':

    avaliacao1 = float (input('Digite sua primeira nota: '))
    while avaliacao1 < 0 or avaliacao1 > 10:
        avaliacao1 = float (input('Nota inválido, digite um valor entre 0 e 10: '))

    avaliacao2 = float (input('Digite sua segunda nota: '))

    while avaliacao2 < 0 or avaliacao2 > 10:
        avaliacao2 = float(input('Nota inválido, digite um valor entre 0 e 10: '))

    soma = avaliacao1 + avaliacao2
    media = soma / 2
    print (media)
    condicao = input('Deseja colocar outra nota? ')