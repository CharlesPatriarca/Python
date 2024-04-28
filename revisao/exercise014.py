horaInicio = int(input('Que horas começou: '))
horaFim = int(input('Que horas terminou: '))

if horaInicio < horaFim:
    hora = horaFim - horaInicio
    #print (f'A partida de xadrez durou {hora}h')
else:
    hora = horaFim + 12 - (horaInicio - 12)
print (f'A partida de xadrez durou {hora}h')