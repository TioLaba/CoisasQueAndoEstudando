from random import choice

'''Busca Binária'''

def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1
    
    # O loop continua enquanto houver elementos a serem examinados
    while esquerda <= direita:
        meio = (esquerda + direita) // 2  # Calcula o índice do meio da sublista
        
        # Verifica se o valor no meio é o alvo
        if lista[meio] == alvo:
            return meio  # Retorna o índice se o alvo for encontrado
        
        # Se o valor do meio for menor que o alvo, ajusta a esquerda
        if lista[meio] < alvo:
            esquerda = meio + 1  # Move o início da sublista para a direita
        
        # Se o valor do meio for maior que o alvo, ajusta a direita
        else:
            direita = meio - 1  # Move o final da sublista para a esquerda
    
    return -1  # Retorna -1 se o alvo não for encontrado

def verificar_resultado(lista, alvo):
    # Chama a função busca_binaria e verifica se o alvo foi encontrado
    resultado = busca_binaria(lista, alvo)

    # Se o alvo for encontrado, retorna o índice
    if resultado != -1:
        return resultado
    else:
        return None  # Retorna None se o alvo não for encontrado

def gerar_lista():
    return [x for x in range(1000000)]  # Gera uma lista de 0 a 999.999

def definir_alvo(lista):
    return choice(lista)  # Escolhe aleatoriamente um valor da lista

# Gera a lista e define o alvo
lista = gerar_lista()
alvo = definir_alvo(lista)

# Verifica o resultado da busca
indice = verificar_resultado(lista, alvo)

# Exibe o resultado final
print(f'O valor desejado "{alvo}" se encontra no índice {indice} da lista.')
