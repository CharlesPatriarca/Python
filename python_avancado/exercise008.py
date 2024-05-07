nomes = ['','','','','']
senhas = ['','','','','']
# numero = 0
para = 12

print ('MENU')
print ('[1] CADASTRO \n [2] LOGIN ')



while para != 1 or para != 2:
    numero = int(input('Digite a opção desejada: '))

    for x in range (5):
        nomes [x] = input(f'Digite seu nome usuário: ')
        senhas [x] = input(f'Digite sua senha usuário: ')
