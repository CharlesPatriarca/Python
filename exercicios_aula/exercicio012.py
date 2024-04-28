#receba do usário um número de 1 a 12 e mostre o nome do mês correspondente.
#Caso o mês não existir, mostrar essa informação '|Valor inválido'.
#Obs.: usando IF/ELIF/ELSE

numero = int (input('Digite o número: '))

if numero < 1 or numero > 12:
    print('Numero invalido')

elif numero == 1:
    print ('Janeiro')
elif numero == 2:
    print ('feveiro')
elif numero == 3:
    print ('Março')
elif numero == 4:
    print ('Abril')
elif numero == 5:
    print ('Maio')
elif numero == 6:
    print ('Junho')
elif numero == 7:
    print ('Julho')
elif numero == 8:
    print ('Agosto')
elif numero == 9:
    print ('Setembro')
elif numero == 10:
    print ('Outubro')
elif numero == 11:
    print ('Novembro')
elif numero == 12:
    print ('Dezembro')