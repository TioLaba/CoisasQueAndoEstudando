# Mantendo estados dentro de classes

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando...')

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotagrar enquanto filma')
        else:
            print(f'{self.nome} está fotografando...')

    # desligar a filamgem
    def parar_filmar(self):
        if self.filmando:
            print(f'{self.nome} Está parando de filmar')
            self.filmando = False
        else:
            print(f'{self.nome} Não esta filmando')

c1 = Camera('Canon')
c2 = Camera('sony')

c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
