menu = 0
while menu != 3:
    print ('Menu')

    print ('[1] - Calcular área do quadrado')
    print ('[2] - Calcular área do triângulo')
    print ('[3] - Calcular área do triângulo')

    menu = int(input('Qual forma geométrica deseja calcular? '))

    if menu == 1:
        areaQ = float(input('Qual o lado do quadrado: '))
        area = areaQ ** 2
        print (f'A área do quadrado é {area}')

    elif menu == 2:
        base = float(input('Digite o valor da base do triângulo: '))
        altura = float(input('Digite o valor da altura do triângulo: '))
        a = (base * altura) / 2
        print (f'A área do triângulo é {a}')

    elif menu == 3:
        print ('Tchau!')