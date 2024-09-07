''' Pilha = ultimo que entra, primeiro que sai'''

class PilhaSimples:
    ''' Essa classe implementa o metodo LIFO para gerenciamento de tarefas.'''
    
    def __init__(self):
        '''Inicia a pilha com uma lista vazia'''
        self.pilha = []

    def adicionar_item(self, item):
        '''Adiciona um  item a pilha
        
        Args:

        item (str): o item a ser adicionado na pilha
        
        '''
        self.pilha.append(item)

    def remover_item(self):
        if self.pilha:
            item_removido = self.pilha.pop()
            print('Item removido', item_removido)
        else:
            print('Pilha Vazia.')

    def exibir_pilha(self):
        pilha = self.pilha
        print('Pilha: ', pilha)

    def exibir_menu(self):
        print('Escolha uma opção:\nObs: Digite apenas numeros.\n')
        print('[1] Adicionar')
        print('[2] Remover')
        print('[3] Exibir')
        print('[0] Sair')

    def obter_escolha(self):
        while True:  # Loop para continuar pedindo entrada até que seja válida
            try:
                escolha = int(input('Escolha (0/1/2/3): '))
                if escolha in [0, 1, 2, 3]:  # Verifica se a escolha está no intervalo permitido
                    self.escolha = escolha
                    return escolha
                else:
                    print('Escolha inválida. Digite apenas números 0/1/2/3.')
            except ValueError:
                print('Entrada inválida. Digite apenas números.')

    def executar(self):
        while True:
            self.exibir_menu()
            escolha = self.obter_escolha()

            if escolha == 1:
                item = input('Adicionar tarefa.')
                self.adicionar_item(item)
            elif escolha == 2:
                self.remover_item()
            elif escolha == 3:
                self.exibir_pilha()
            elif escolha == 0:
                break

pilha = PilhaSimples()
pilha.adicionar_item('vlr')
pilha.adicionar_item('vlr1')
pilha.adicionar_item('vlr2')
pilha.exibir_pilha()
pilha.remover_item()
pilha.remover_item()
pilha.exibir_pilha()

            