# Faça um código que receba as 3 notas de um aluno

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print('Aprovado')
else:
    print("Reprovado")

# altere o código anterior e acrescente a opção de aluno em recuperação, caso sua média seja menor que 7,0 e maior que 4,0

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
else:
    if media < 4:
        print("reprovado")
    else:
        print("recuperração")