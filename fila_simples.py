def adicionar_item(fila, item):
    fila.append(item)
    print('Item adicionado:', item)
    return fila

def remover_item(fila):
    if fila:
        item_removido = fila.pop(0)  # Remove o primeiro item da fila (fifo)
        print('Item removido:', item_removido)
    else:
        print('A fila está vazia!')
    return fila

def armazenar_items(fila=[]):
    return fila

def executar():
    '''Essa função processa as funções e retorna uma lista'''
    fila = armazenar_items()
    while True:
        print('\nEscolha:')
        print('[1] adicionar')
        print('[2] remover')
        print('[3] exibir')
        print('[0] sair')
        try:
            escolha = int(input('Escolha uma opção: '))
        except ValueError:
            print('Por favor, insira um número inteiro válido.')
            continue
        
        if escolha == 1:
            item = input('Adicionar Tarefa: ')
            fila = adicionar_item(fila, item)
        
        elif escolha == 2:
            fila = remover_item(fila)
        
        elif escolha == 3:
            print('Fila atual:', fila)

        elif escolha == 0:
            print('Saindo...')
            break

        else:
            print('Escolha apenas números inteiros.')

    print('Fim de execução')
    return fila

if __name__ == '__main__':
    fila_final = executar()
    print('Estado final da fila:', fila_final)
