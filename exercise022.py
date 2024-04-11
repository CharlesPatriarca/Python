#receber numero de aluno
alunos = int(input('Quantos alunos? '))
alunosVerificados = 0
soma = 0

#solicitar as notas dos aluno
while alunosVerificados < alunos:
    notas = float(input("Natas dos alunos: "))
    soma = soma + notas
    alunosVerificados += 1
media = soma / alunos
print(media)