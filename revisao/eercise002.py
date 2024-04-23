condicao = 'S'

while condicao == 'S' or 's':
    num = int(input('Digite um número: '))

    if num > 0:
        print(f'{num} é positivo')
    elif num == 0:
        print(f'{num} é neutro')
    else:
        print(f'{num} é negativo')

    condicao = input('Deseja continuar? ')
