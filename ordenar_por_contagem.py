def ordenar_por_contagem(lista):
    # Encontrar o valor mais alto da lista para definir o tamanho da lista de contagem
    valor_maximo = max(lista)

    # Criar a lista de contagem com zeros. O tamanho é baseado no valor máximo + 1,
    # pois a contagem deve ter um índice para cada valor possível na lista.
    contagem = [0] * (valor_maximo + 1)

    # Remover os itens da lista original e contar quantas vezes cada número aparece
    while len(lista) > 0:  # Enquanto houver itens na lista original
        numero = lista.pop(0)  # Remove o primeiro valor da lista e armazena na variável 'numero'
        contagem[numero] += 1  # Incrementa o valor no índice correspondente na lista de contagem

    # Recriar a lista original, mas agora em ordem crescente
    for i in range(len(contagem)):  # Itera sobre cada índice da lista de contagem
        while contagem[i] > 0:  # Enquanto o valor no índice atual da contagem for maior que 0
            lista.append(i)  # Adiciona o índice 'i' à lista, o que representa o valor ordenado
            contagem[i] -= 1  # Decrementa o valor no índice atual da lista de contagem

    return lista  # Retorna a lista ordenada


from selection_sort import gerar_lista  # essa função gera uma lista

if __name__ == '__main__':
    lista = ordenar_por_contagem(gerar_lista()) 
    print('Lista contagem: ', lista)
    print('Tamanho da lista:', len(lista))