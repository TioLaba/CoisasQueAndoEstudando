from random import shuffle, randint


def obter_menor_valor(lista):
    menor_valor = lista[0]

    for item in lista:
        if item < menor_valor:
            menor_valor = item
    
    return menor_valor

def gerar_lista():
    lista = [randint(x, 100) for x in range(1, 10)]
    shuffle(lista)
    return lista

if __name__ == '__main__':
    lista = gerar_lista()
    menor_valor = obter_menor_valor(lista)
    print('O menor valor dessa lista é ', menor_valor)