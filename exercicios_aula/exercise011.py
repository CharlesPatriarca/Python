# / -> divisão
# // -> inteiro da divisão
# % resto da divisão (módulo)

# expressões Aritméticas - MOD
# Receba um número, do usuário e diga se ele é par ou ímpar

number1 = int(input('Digite um número: '))

if number1 % 2 == 0:
    print (f'{number1} é um número par.')
else:
    print (f'{number1} é um número ímpar.')