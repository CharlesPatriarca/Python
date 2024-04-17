litros = float(input('Quantos litros você abasteceu? '))
combs = input('Qual combustível você utilizou? ')
E_etanol = 4.90
G_gasolina = 5.80

if combs == "E" or combs == "e":
    total = litros * E_etanol
    print('Total gasto', total)
elif combs == "G" or combs =="g":
 total = litros * G_gasolina
 print('Total gasto', total)
else:
    print ('Combustível inválido')