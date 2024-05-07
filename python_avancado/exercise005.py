a = [0,0,0,0,0,0,0,0,0,0]
m = [0,0,0,0,0,0,0,0,0,0]
guar = 0

for y in range (10):
    a[y] = int(input('Digite um número: '))

x = int(input('Digite o multiplicador: '))

for mult in range (len(a)):
    m[mult] = a[mult] * x


print (a)
print (x)
print (m)
