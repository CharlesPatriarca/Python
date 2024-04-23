num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    print (f'{num1}, é o maior deles')
elif num2 > num1 and num1 > num3:
    print (f'{num2} é o maior deles')
else:
    print (f'{num3} é o maior deles')