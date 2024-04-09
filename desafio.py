# Dados os valores de horários abaixo, decifre a lógica e faça um código para executar.
# entrada01 = 3:45 (recebe primeiro a hora e depois o minuto)
# entrada = 14:20 (recebe primeiro a hora e depois o minuto)

# saída = 6:05

hora1 = int(input('Digite a primeira hora: '))
minuto1 = int(input('Agora digite os minutos: '))
hora2 = int(input('Digite a hora: '))
minuto2 = int(input('Agora digite os minutos: '))

if hora1 > 12:
    hora1 = hora1 - 12

if hora2 > 12:
    hora2 = hora2 - 12

horas = hora1 + hora2
if horas > 12:
    horas = horas - 12

minutos = minuto2 + minuto2

if minutos >= 60:
    minutos = minutos - 60
    horas = horas + 1

print (horas, ':',minutos)