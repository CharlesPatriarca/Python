class Pessoa():
    def __init__(self, nomeAluno, pesoAluno, idadeAluno):
        self.nome = nomeAluno
        self.peso = pesoAluno
        self.idade = idadeAluno
        self.comendo = False
        self.falando = True
        self.dormindo = True
        self.pararComer = True
        self.acordando = True
        self.naoFale = False

    def comer(self, comida, bebida):
        if self.comendo == True:
            print(f'{self.nome} não pode falar e nem dormir, deve continuar comendo sua {comida} e tomando seu {bebida}')
        else:
            self.comendo == False
            print(f'{self.nome} já pode falar ou dormir, teminou de comer.')

    def falar(self):
        if  self.falando == True:
            print(f'{self.nome} deve parar de falar para poder comer ou dormir')
        else:
            self.falando == False
            print (f'{self.nome} pode ir dormir ou comer, pois parou de falar')

    def dormir(self):
        if self.dormindo == True:
            print(f'{self.nome} está dormindo, não incomode ele.')
        else:
            self.comendo == False
            print(f'{self.nome} pode comer ou falar, porque não está dormindo')

    def pareComer(self, comida, bebida):
        if self.pararComer == True:
            print(f'{self.nome} você deve parar de comer a {comida} e o {bebida}')
        else:
            print(f'{self.nome} pode continuar comendo')
    def acordar(self):
        if self.acordando == True:
            print(f'{self.nome} acorde parar comer.')
        else:
            self.comendo == False
            print(f'{self.nome} já ta gordinho, não precisa acordar pra comer')

    def pararFalar(self):
        if self.naoFale == True:
            print(f'{self.nome} ninguém quer ouvir você não fale mais')
        else:
            self.naoFale == False
            print(f'{self.nome} pode começar a falar')


class Banco():

    def __init__(self, clienteNome, numeroConta, tipoConta):
        self.clienteNome = clienteNome
        self.numeroConta = numeroConta
        self.tipoConta = tipoConta
        self.saldo = 0.00
        self.statusConta = False

    def ativarConta(self):
        if self.statusConta == False:
            self.statusConta = True
            print('Conta ativada com sucesso')
        else:
            print('Conta já está ativada')

    def desativarConta(self):
        if self.statusConta == True:
            if self.saldo == 0:
                self.statusConta = False
                print('Conta desativada com sucesso')
            else:
                print('Não é possível desativar, ainda possui saldo')
        else:
            print('Conta já está desativada')

    def depositar(self):
        if self.statusConta == False:
            print('Sua conta está desativada, não pode depositar')
            self.statusConta = True
        else:
            print('Pode depositar')

    def sacar(self, saldo):
        if saldo > self.saldo:
            print('Pode sacar seu dinheiro')
        else:
            print('Saldo zerado, não pode sacar')


class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f'{self.nome} sem comida hoje')


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f'O {self.nome} está miando')

    def latir1(self):
        print('Seu gato esta possesso, ele está latindo')


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f'O {self.nome} está latindo')


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def roer(self):
        print(f'O {self.nome} está roendo')


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def muje(self):
        print(f'O {self.nome} está mujindo')


class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0


class Retangulo(Forma):
    def __init__(selfo):
        super().__init__()

    def calcularArea(self, base, altura):
        self.area = base * altura
        print(f'A área do retângulo é {self.area}')

    def calcularPerimetro(self, base, altura):
        self.perimetro = (base + altura) * 2
        print(f'O perímetro do retângulo é {self.perimetro}')


class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def areaTriangulo(self, base, altura):
        self.area = (base * altura) // 2
        print(f'A area do triangulo é {self.area}')

    def perimetroTriangulo(self, l1, l2, l3):
        self.perimetro = l1 + l2 + l3
        print(f'Perimetro igual a {self.perimetro}')


class Atleta():
    def __init__(self):
        self.aposentado = True
        self.peso = 52

    def aposentar(self):
        if self.aposentado == True:
            print(f'Atleta já está aposentado')
        else:
            print(f'Atleta ainda pode competir')

    def peso(self):
        print(f'O peso do atleta ')


class Corredor(Atleta):
    def __init__(self):
        super().__init__()


class Ingresso ():
    def __init__(self, valor):
        self.valor = valor
        
    def imprimeValor(self):
        print (f'Valor do ingresso normal é R$ {self.valor}')

class IngressoVip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)


    def imprimeValor(self):
        valorVip = self.valor * 1.5
        print(f'R$ {valorVip}')






















