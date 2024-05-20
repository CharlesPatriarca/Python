class Pessoa():
    def __init__(self, nomeAluno, pesoAluno, idadeAluno, comendo = False):
        self.nome = nomeAluno
        self.peso = pesoAluno
        self.idade = idadeAluno

    def comer(self, comida, bebida):
        print (f'{self.nome} foi comer {comida} com {bebida}')

    def falar(self, cafe, smartphone):
        print (f'{self.nome} esta falando com {cafe} pelo {smartphone}')

    def dormir(self, horario):
        print (f'{self.nome} dormiu às {horario}')

    # def pareComer(self):
    #
    # def acordar(self):
    #
    # def pararFalar(self):