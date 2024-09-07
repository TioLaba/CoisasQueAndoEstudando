import time
from random import randint

def gerar_lista(tamanho):
    return [randint(1, tamanho) for _ in range(tamanho)]

# Lista de exemplo
lista = gerar_lista(10000)

# Medindo o tempo para Selection Sort
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        menor_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor_index]:
                menor_index = j
        lista[i], lista[menor_index] = lista[menor_index], lista[i]
    return lista

# Medir o tempo do Selection Sort
start_time = time.time()
selection_sort(lista.copy())
print("Tempo Selection Sort:", time.time() - start_time)

# Medindo o tempo para sorted()
start_time = time.time()
sorted(lista)
print("Tempo sorted():", time.time() - start_time)
