nomes = ['','','','','']
senhas = [0,0,0,0,0]

for x in range (5):
    nomes [x] = input(f'Digite seu nome usuário {x + 1}: ')
    senhas [x] = input(f'Digite sua senha usuário {x + 1}: ')

for y in range (5):

    print(f'O usuário {y} - {nomes[y]} é {senhas[y]}')