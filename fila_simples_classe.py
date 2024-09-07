class Fila:
    """Classe que implementa uma fila (FIFO) para gerenciamento de tarefas."""
    
    def __init__(self):
        """Inicializa a fila como uma lista vazia."""
        self.fila = []

    def adicionar_item(self, item):
        """Adiciona um item à fila.

        Args:
            item (str): O item a ser adicionado à fila.
        """
        self.fila.append(item)
        print(f'Item adicionado: {item}')

    def remover_item(self):
        """Remove o primeiro item da fila (FIFO) e o exibe.

        Se a fila estiver vazia, exibe uma mensagem de alerta.
        """
        if self.fila:
            item_removido = self.fila.pop(0)
            print(f'Item removido: {item_removido}')
        else:
            print('A fila está vazia!')

    def exibir_fila(self):
        """Exibe o estado atual da fila."""
        if self.fila:
            print('Fila atual:', ', '.join(self.fila))
        else:
            print('A fila está vazia!')

        """Inicia o loop de interação com o usuário para manipulação da fila."""
        while True:
            self._exibir_menu()
            escolha = self._obter_escolha_do_usuario()

            if escolha == 1:
                item = input('Adicionar Tarefa: ')
                self.adicionar_item(item)
            elif escolha == 2:
                self.remover_item()
            elif escolha == 3:
                self.exibir_fila()
            elif escolha == 0:
                print('Saindo...')
                break
            else:
                print('Escolha inválida. Por favor, tente novamente.')

        print('Fim de execução')

    @staticmethod
    def _exibir_menu():
        """Exibe o menu de opções para o usuário."""
        print('\nEscolha:')
        print('[1] Adicionar')
        print('[2] Remover')
        print('[3] Exibir')
        print('[0] Sair')

    @staticmethod
    def _obter_escolha_do_usuario():
        """Obtém e valida a escolha do usuário.

        Returns:
            int: A escolha do usuário.
        """
        while True:
            try:
                return int(input('Escolha uma opção: '))
            except ValueError:
                print('Por favor, insira um número inteiro válido.')


if __name__ == '__main__':
    fila = Fila()
    fila.exibir_fila()
    print('Estado final da fila:', fila.fila)
