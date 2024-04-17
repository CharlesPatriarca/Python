# ler o nome de 2 times e o número de gols marcos na partida (para cada time). Escrever o nome do vencedor.
# Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time1 = input('Nome do time: ')
golt1 = int(input('Gols do time: '))
time2 = input('Nome do time: ')
golt2 = int(input('Gols do time: '))

if golt1 == golt2:
    print('Deu empate')
elif golt1 > golt2:
    print(f'O {time1} ganhou de lavada')
else:
    print(f'O {time2} ganhou de lavada')
