'''

### **Teste de Recrutamento: Programador Intermediário**

#### **Seção 1: Lógica de Programação e Algoritmos**

1. **Problema: Fila com Prioridade**
   
   - Implemente uma fila com prioridade utilizando uma estrutura de dados apropriada. A fila deve permitir a inserção de 
   elementos com uma prioridade associada e deve remover sempre o elemento de maior prioridade.
  
    - **Requisitos:**
     - Cada elemento inserido na fila deve ser um par `(valor, prioridade)`.
     - Deve ser possível inserir elementos com prioridade e remover o elemento com a maior prioridade.
     - Se dois elementos tiverem a mesma prioridade, o elemento inserido primeiro deve ser removido primeiro 
     (comportamento FIFO).
   
   - **Exemplo de Uso:**
     ```python
     fila = FilaPrioridade()
     fila.inserir("tarefa1", 1)
     fila.inserir("tarefa2", 3)
     fila.inserir("tarefa3", 2)
     print(fila.remover())  # Output: "tarefa2"
     print(fila.remover())  # Output: "tarefa3"
     print(fila.remover())  # Output: "tarefa1"
     ```
'''
class FilaComPrioridade:
    def __init__(self):
        self.fila = []

    def inserir(self, valor, prioridade):
        """Adiciona um elemento com sua respectiva prioridade na fila."""
        self.fila.append((valor, prioridade))
        print(f'{(valor, prioridade)} adicionado com sucesso.')

    def remover(self):
        """Remove o elemento com a maior prioridade da fila."""
        if self.fila:
            self.ordenar_fila_prioridade()  # Ordenar a fila antes de remover
            removido = self.fila.pop(0)
            print(f'{removido} removido com sucesso.')
        else:
            print('Fila vazia')

    def obter_tarefa(self):
        """Obtém a tarefa do usuário."""
        tarefa = input('Informe a tarefa: ')
        return tarefa

    def obter_prioridade(self):
        """Obtém a prioridade da tarefa do usuário, garantindo que seja um número entre 1 e 5."""
        while True:
            try:
                prioridade = int(input('Defina a prioridade da tarefa (1 a 5, sendo 5 a máxima): '))
                if 1 <= prioridade <= 5:
                    return prioridade
                else:
                    print('Erro: Digite um número entre 1 e 5.')
            except ValueError:
                print('Erro: Digite apenas números de 1 a 5.')

    def ordenar_fila_prioridade(self):
        """Ordena a fila de acordo com a prioridade (maior prioridade primeiro)."""
        self.fila.sort(key=lambda x: x[1], reverse=True)  # Prioridade é o segundo elemento da tupla

    def exibir_fila(self):
        """Exibe o estado atual da fila."""
        if self.fila:
            print('Fila atual:', ', '.join([f'{item[0]}(prioridade: {item[1]})' for item in self.fila]))
        else:
            print('A fila está vazia!')

    def exibir_menu(self):
        """Exibe o menu de opções para o usuário."""
        print('\nEscolha:')
        print('[1] Adicionar')
        print('[2] Remover')
        print('[3] Exibir')
        print('[0] Sair')

    def obter_escolha(self):
        """Obtém e valida a escolha do usuário."""
        while True:
            try:
                return int(input('Escolha uma opção: '))
            except ValueError:
                print('Por favor, insira um número inteiro válido.')

    def iniciar(self):
        """Inicia o loop de interação com o usuário para manipulação da fila."""
        while True:
            self.exibir_menu()
            escolha = self.obter_escolha()

            if escolha == 1:
                tarefa = self.obter_tarefa()
                prioridade = self.obter_prioridade()
                self.inserir(tarefa, prioridade)
                self.ordenar_fila_prioridade()
            elif escolha == 2:
                self.remover()
            elif escolha == 3:
                self.exibir_fila()
            elif escolha == 0:
                print('Saindo...')
                break
            else:
                print('Escolha inválida. Por favor, tente novamente.')

        print('Fim de execução')

if __name__ == "__main__":
    fila = FilaComPrioridade()
    # fila.iniciar()
    fila.inserir("tarefa1", 1)
    fila.inserir("tarefa2", 3)
    fila.inserir("tarefa3", 2)
    fila.remover()  # Output: "tarefa2"
    fila.remover()  # Output: "tarefa3"
    fila.remover()  # Output: "tarefa1"
