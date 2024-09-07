from random import randint

def gerar_lista():
    lista = set()
    for x in range(1000):
        x = randint(1, 10000)
        lista.add(x)
    
    return list(lista)

lista = gerar_lista()

def ordenar_por_selecao(lista):

    n = len(lista)

    for i in  range(n): # j representa o inicio da parte não ordenada da lista
        menor_valor = i # agente assume que o menor valor começa na posição i

        for j in range(i + 1, n):
            if lista[j] < lista[menor_valor]: # se o primeiro valor da parte não ordenada for menor que o ultimo valor da parte ordenada
                menor_valor = j

        lista[i], lista[menor_valor] = lista[menor_valor], lista[i]  # troca o valor anterior da parte ordenada pelo menor valor atual

    return lista

if __name__ == '__main__':
    ordenar = ordenar_por_selecao(lista)
    print(ordenar) 