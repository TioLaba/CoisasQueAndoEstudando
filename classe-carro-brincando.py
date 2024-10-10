from time import sleep
from keyboard import is_pressed

# Constantes
MAX_VELOCIDADE = 180
MAX_VELOCIDADE_RE = 20

class Carro:
    def __init__(self, nome, velocidade=0, velocidade_re=0):
        self.nome = nome
        self.velocidade = velocidade
        self.velocidade_re = velocidade_re
        
    def acelerar(self):
        if self.velocidade_re > 0:
            print(f'\tFreie o {self.nome} antes de acelerar: {self.velocidade_re} km/h em marcha ré')
            self.velocidade_re -= 1
        else:
            if self.velocidade < MAX_VELOCIDADE:
                self.velocidade += 1
                print(f'\t{self.velocidade} km/h')
            else:
                print(f'\t{self.nome} já está na velocidade máxima: {self.velocidade} km/h')
            
    def freiar(self):
        if self.velocidade > 0:
            self.velocidade -= 1
            print(f'\t{self.velocidade} km/h')
        else:
            print(f'\t{self.nome} já está parado.')
    
    def virar_esquerda(self):
        print(f'\tVirando {self.nome} para esquerda\n<<<<<<<<<<')
    
    def virar_direita(self):
        print(f'\tVirando {self.nome} para direita\n>>>>>>>>>>')
    
    def marcha_re(self):
        print('\tMarcha ré')
        if self.velocidade > 0:
            print(f'\tFreie o {self.nome} antes de dar ré: {self.velocidade} km/h')
            self.velocidade -= 1
        else:
            if self.velocidade_re < MAX_VELOCIDADE_RE:
                self.velocidade_re += 1
                print(f'\t{self.nome} dando ré: {self.velocidade_re} km/h')
            else:
                print(f'\t{self.nome} já está na velocidade máxima em marcha ré: {self.velocidade_re} km/h')

golf = Carro('Golf')

# Variáveis de controle 
stop = True

print('_' * 30)
print('Testando objetos de classes\n')
print('[ W ] Acelerar')
print('[   ] Freiar ')
print('[ S ] Marcha ré')
print('[ D ] Direita')
print('[ A ] Esquerda')
print('[ Q ] Sair')
print('_' * 30, '\n')

while stop:
    if is_pressed('w'):
        golf.acelerar()
        sleep(0.1)  # Controle de taxa de aceleração
    elif is_pressed(' '):
        golf.freiar()
        sleep(0.1)  # Para evitar múltiplas chamadas rápidas
    elif is_pressed('s'):
        golf.marcha_re()
        sleep(0.1)
    elif is_pressed('d'):
        golf.virar_direita()
        sleep(0.1)
    elif is_pressed('a'):
        golf.virar_esquerda()
        sleep(0.1)
    elif is_pressed('q'):
        stop = False

print('\nFim de Teste')
