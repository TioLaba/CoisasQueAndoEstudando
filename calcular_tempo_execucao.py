import time
from inserction_sort import gerar_lista, ordenacao_por_insercao
from selection_sort import ordenar_por_selecao
from quick_sort import quicksort
from counting_sort import contagemOrdenacao


'''A ideia é comparar a eficiencia de diferentes estruturas de ordenação calculando o tempo de execução'''
def calcular_tempo(funcao, *args, **kwargs):
    """
    Calcula o tempo de execução de uma função com os parâmetros fornecidos.
    """
    inicio = time.time()  # Marca o tempo inicial
    funcao(*args, **kwargs)  # Executa a função com os parâmetros fornecidos
    fim = time.time()  # Marca o tempo final
    tempo = fim - inicio  # Calcula o tempo de execução

    # Converte o tempo de execução para horas, minutos e segundos
    horas = int(tempo // 3600)
    minutos = int((tempo % 3600) // 60)
    segundos = int(tempo % 60)

    # Retorna o tempo de execução formatado
    return f"{horas}h {minutos}m {segundos}s"

# Cria uma lista de funções e seus argumentos
funcoes = [
    (contagemOrdenacao, gerar_lista()),        # Para contagemOrdenacao
    (quicksort, gerar_lista(), 0, 9),         # Para quicksort com início e fim da lista
    (ordenacao_por_insercao, gerar_lista()),  # Para ordenacao_por_insercao
    (ordenar_por_selecao, gerar_lista()),     # Para ordenar_por_selecao
]

# Calcula e exibe o tempo de execução para cada função
for funcao, *args in funcoes:
    print(f"Tempo de execução de {funcao.__name__}: {calcular_tempo(funcao, *args)}")
