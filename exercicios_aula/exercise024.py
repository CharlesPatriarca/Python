senha = 'dog123'
tentativa = input('Digite sua senha: ')
tentativas = 1

while tentativas < 3:
    if senha == tentativa:
        print ('Login efetuado com sucesso')
        break
        # tentativas = 4
    else:
        senha = input('Senha incorreta, digite novamente: ')
        tentativas += 1

    if tentativas == 3:
        print('Acesso negado')
        break







