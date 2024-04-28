h1 = int(input('Digite a hora: '))
m1 = int(input('Digite os minutos: '))

h2 = int(input('Digite a hora: '))
m2 = int(input('Digite os minutos: '))

hSoma = h1 + (h2 -12)
mSoma = m1 + m2

if mSoma >= 60:
    hSoma + 1
    print (f'{hSoma}:{mSoma}')
else:
    print (f'{hSoma}:{mSoma}')