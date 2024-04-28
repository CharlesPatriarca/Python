eleitores = int(input('Quantos eleitores? '))
votoBranco = int(input('Quantos votos brancos? '))
votoNulo = int(input('Quantos votos nulos? '))
votoValido = int(input('Quantos votos válidos? '))

porc = 100
pVotoBranco = votoBranco / eleitores * porc
pVotoNulo = votoNulo / eleitores * porc
pVotoValido =  votoValido / eleitores * porc

print (eleitores)
print (pVotoBranco)
print (pVotoNulo)
print (pVotoValido)