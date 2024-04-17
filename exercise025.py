avaliacao1 = float (input('Digite sua primeira nota: '))

while avaliacao1 < 0 or avaliacao1 > 10:
    avaliacao1 = float (input('Nota inválido, digite um valor entre 0 e 10: '))

avaliacao2 = float (input('Digite sua segunda nota: '))

while avaliacao2 < 0 or avaliacao2 > 10:
    avaliacao2 = float(input('Nota inválido, digite um valor entre 0 e 10: '))

soma = avaliacao1 + avaliacao2
media = soma / 2

print (f'Sua média foi: {media}')

if media < 7 and media > 4:
    print ('Você está em recuperação')
elif media < 4:
    print ('Você foi reprovado')
else:
    print ('Você está aprovado')



