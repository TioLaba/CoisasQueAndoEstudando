from random import shuffle

def gerar_lista():
    ''' O bjetivo dessa lista gigante, é ser usada como meio de comparação
    de eficiencia e tempo encontrado no arquivo calcular_tempo_execucao.py'''
    # Gera uma lista com números de 1 a 50.000 e embaralha os números
    lista = [x for x in range(1, 50000)]  # Cria uma lista com números de 1 a 999
    shuffle(lista)  # Embaralha a lista para garantir uma ordem aleatória
    return lista  # Retorna a lista embaralhada

def ordenacao_por_insercao(lista):
    n = len(lista)  # Obtém o comprimento da lista, ou seja, o número total de elementos
    
    # Loop externo: percorre a lista a partir do segundo elemento (índice 1)
    for i in range(1, n):
        valor_atual = lista[i]  # Armazena o valor que será inserido na parte classificada da lista
        j = i - 1  # Inicia o índice `j` para percorrer a parte classificada da lista de trás para frente
        
        # Loop interno: move elementos da parte classificada que são maiores que valor_atual
        while j >= 0 and lista[j] > valor_atual:
            # Desloca o elemento para a direita
            lista[j + 1] = lista[j]  # Move o elemento maior para a posição seguinte
            j -= 1  # Move para o próximo elemento da sublista classificada
        
        # Coloca valor_atual na posição correta dentro da parte classificada
        lista[j + 1] = valor_atual  # Insere o valor atual na posição encontrada
    
    return lista  # Retorna a lista ordenada

if __name__ == '__main__':
    lista = gerar_lista()  # Gera uma lista aleatória
    print("Lista não ordenada:", lista)  # Mostra a lista antes da ordenação
    lista_ordenada = ordenacao_por_insercao(lista)  # Ordena a lista usando o algoritmo Insertion Sort
    print("Lista ordenada:", lista_ordenada)  # Mostra a lista ordenada
