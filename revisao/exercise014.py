horaInicio = int(input('Que horas começou: '))
horaFim = int(input('Que horas terminou: '))

if horaInicio < horaFim:
    hora = horaFim - horaInicio
    print (f'A partida de xadrez durou {hora}h')
else:
    hora1 = horaFim + 12 - (horaInicio - 12)
    print (f'A partida de xadrez durou {hora1}h')