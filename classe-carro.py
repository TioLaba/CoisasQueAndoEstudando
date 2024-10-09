class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} Está acelerando ...')

    def freiar(self):
        print(f'{self.nome} Está freiando ...')


# Entendendo os metodos 
fusca = Carro('Fusquinha')
fusca.acelerar()
fusca.freiar()