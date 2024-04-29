eleitores = int(input('Numero de eleitores: '))
brancos = int(input('Numero de brancos: '))
nulos = int(input('Numero de nulos: '))
validos = int(input('Numero de válidos: '))

porcE = 100
porcB = brancos / eleitores * 100
porcN = nulos / eleitores * 100
porcV = validos / eleitores * 100

print()
print(f'{porcB}%')
print(f'{porcN}%')
print(f'{porcV}%')