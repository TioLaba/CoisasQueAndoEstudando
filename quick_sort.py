from inserction_sort import gerar_lista

# treinando quick sort
def particionar(lista, inicio, fim):
    pivo = lista[fim] # escolher o pivo ( sendo o ultimo elemento da lista)
    i = inicio - 1 # indice para separar os elmentos menores que o pivo

    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]  # Coloca o pivô na posição correta
    return i + 1 # posição pivo

def quicksort(lista, inicio, fim):
    if inicio < fim:
        índice_pivô = particionar(lista, inicio, fim)  # Particiona a lista e acha a posição do pivô
        quicksort(lista, inicio, índice_pivô - 1)  # Aplica Quicksort na parte esquerda
        quicksort(lista, índice_pivô + 1, fim)  # Aplica Quicksort na parte direita

if __name__ == '__main__':
    # Exemplo de uso
    lista = gerar_lista()
    print('lista gerada:')
    print(lista)
    quicksort(lista, 0, len(lista) - 1)
    print('lista ordenada:')
    print(lista)  # Saída: [2, 3, 5, 6, 8]
