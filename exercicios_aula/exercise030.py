notasAlunos = ['','','','','']
soma = 0
media = 0
acimaMedia = 0

for x in range (len(notasAlunos)):
    notasAlunos[x] = float(input('Digite a nota dos alunos: '))

for y in range (len(notasAlunos)):
    soma = soma + notasAlunos [y]
    media = soma / len (notasAlunos) #ou 5

for p in range (len(notasAlunos)):
    if notasAlunos[p] >= media:
        acimaMedia += 1

print (f'A média da turma foi {media} e a quantidade de alunos acima da média foi {acimaMedia}')