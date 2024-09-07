from random import shuffle

def gerar_lista():
    lista = [x for x in range(1, 1000)]  # Cria uma lista de 1 a 999
    shuffle(lista)  # Embaralha a lista
    return lista

def bubble_sort(lista):
    n = len(lista)  # Obtém o tamanho da lista

    for indice in range(n-1):  # Loop externo para passar pela lista n-1 vezes
        trocas_feitas = False  # Inicializa a variável para verificar se houve troca nesta passagem
        
        for proximo_indice in range(n-indice-1):  # Loop interno para comparar elementos adjacentes
            
            if lista[proximo_indice] > lista[proximo_indice + 1]:  # Compara elementos
                lista[proximo_indice], lista[proximo_indice + 1] = lista[proximo_indice + 1], lista[proximo_indice]  # Troca se necessário
                trocas_feitas = True  # Marca que houve uma troca
        
        if not trocas_feitas:  # Se nenhuma troca foi feita, a lista já está ordenada
            break

    return lista

if __name__ == '__main__':
    lista = gerar_lista()  # Gera uma lista embaralhada
    print("Lista original:")
    print(lista)  # Imprime a lista original
    ordenar = bubble_sort(lista)  # Ordena a lista usando Bubble Sort
    print("Lista ordenada:")
    print(ordenar)  # Imprime a lista ordenada
