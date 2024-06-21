def imprime_nome (nome): # assinatura da função
    print (f'Nome: {nome}')
    imprime_nome('Charles')
    imprime_nome('Isabelly')
    imprime_nome('Helena')

def piramide (num):
    for n in range (1, num + 1):
        for x in range (1, n+1):

            print (n, end=' ')
        print ()

def piramide2 (num):
    for z in range (1, num + 1):
        for x in range (1, z + 1):
            print (x, end=' ')
        print ()

def texto (texto):
    cont = 0
    for x in texto:
        if x in 'aeiouAEIOU':
            cont = cont + 1
    print(cont)

def estoque (nome, quantidade, valor):
    total = quantidade * valor
    return total

def argumeto (valor):
    if valor > 0:
        return 'P'
    elif valor < 0:
        return 'N'
    else:
        return 'Z'

def estoqueDesafio (nome, quantidade, valor):
    total = quantidade * valor
    return total

def somar (num1, num2):
    soma = num1 + num2
    # return num1 + num2
    return soma

def somar2 (*num):
    # tupla (1, 2, 3, 4,...)
    soma = 0
    for x in range (len(num)):
        soma += num[x]
    return soma
def contadorTexto (text):
    caracter = 0

    for y in range (len(text) - 1, -1, -1):
        print (text[y], end = ' ')
        if text[y] == " " or text[y] == "." or text[y] == "!" or text[y] == ",":
            caracter += 1
    print()
    print (len(text) - caracter)
def numeros (array):
    # novaLista = []
    # for x in array:
    #     if x not in novaLista:
    #         novaLista.append(x)
    # print(array)
    # print(novaLista)
    novaLista = set (array)
    print (novaLista)

def number (primo):
    if primo == 1:
        return 'Não'
    elif primo == 2:
        return 'Não'
    else:
        for x in range (2, primo):
            if primo % x == 0:
                return 'Não'
        return 'Primo'