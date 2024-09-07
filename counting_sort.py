def contagemOrdenacao(lista):
    # Acha o maior valor da lista para criar o array de contagem do tamanho certo
    maior_valor = max(lista)
    
    # Cria a lista de contagem com zeros
    contagem = [0] * (maior_valor + 1)

     # Conta quantas vezes cada número aparece
    while len(lista) > 0:
        numero = lista.pop(0)
        contagem[numero] += 1

    # Recria a lista original, mas agora em ordem
    for i in range(len(contagem)):
        while contagem[i] > 0:
            lista.append(i)
            contagem[i] -= 1

    return lista

if __name__ == '__main__':
    # Exemplo de uso
    listaNaoOrdenada = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
    listaOrdenada = contagemOrdenacao(listaNaoOrdenada)
    print("Lista ordenada:", listaOrdenada)
