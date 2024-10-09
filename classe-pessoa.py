# entendendo conceitos de classes POO

class Pessoa:
    # metodo construtor
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    

# instanciando os objetos
p1 = Pessoa('Valter', "Tertuliano")
print(p1.nome)
print(p1.sobrenome)