anoAtual = 2024

idade = int(input('Digite sua idade: '))
niver = input('Você já fez aniversário:  ')

if niver == 'S' or niver == 's':
    nascimento = anoAtual - idade
else:
    nascimento = anoAtual - idade - 1

print(f'Você nasceu no ano {nascimento}')
