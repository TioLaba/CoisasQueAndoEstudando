# Função para mesclar (merge) dois sub-arrays de forma ordenada
def mesclar(esquerda, direita):
    resultado = []  # Lista para armazenar o resultado final
    i = j = 0  # Índices para percorrer as listas esquerda e direita

    # Enquanto houver elementos em ambos os sub-arrays
    while i < len(esquerda) and j < len(direita):
        # Comparando os elementos dos sub-arrays
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])  # Adiciona o menor elemento ao resultado
            i += 1  # Avança o índice do sub-array da esquerda
        else:
            resultado.append(direita[j])  # Adiciona o menor elemento ao resultado
            j += 1  # Avança o índice do sub-array da direita

    # Adiciona os elementos restantes do sub-array da esquerda (se houver)
    resultado.extend(esquerda[i:])

    # Adiciona os elementos restantes do sub-array da direita (se houver)
    resultado.extend(direita[j:])

    return resultado  # Retorna o array mesclado e ordenado

# Função para implementar o algoritmo Merge Sort
def ordenacaoMesclar(arr):
    # Caso base: se o array tem 1 ou 0 elementos, já está ordenado
    if len(arr) <= 1:
        return arr

    # Dividindo o array ao meio
    meio = len(arr) // 2  # Calcula o índice do meio do array
    metadeEsquerda = arr[:meio]  # Sub-array da esquerda
    metadeDireita = arr[meio:]  # Sub-array da direita

    # Chamada recursiva para ordenar as duas metades
    esquerdaOrdenada = ordenacaoMesclar(metadeEsquerda)  # Ordena a metade esquerda
    direitaOrdenada = ordenacaoMesclar(metadeDireita)  # Ordena a metade direita

    # Mesclando os sub-arrays já ordenados
    return mesclar(esquerdaOrdenada, direitaOrdenada)  # Retorna o array mesclado e ordenado

# Testando o algoritmo com um array desordenado
arrayDesordenado = [3, 7, 6, -10, 15, 23.5, 55, -13]  # Array que será ordenado
arrayOrdenado = ordenacaoMesclar(arrayDesordenado)  # Ordena o array usando Merge Sort

# Exibindo o array ordenado
print("Array ordenado:", arrayOrdenado)  # Mostra o array ordenado no console

'''

Na prática, a função `sorted()` do Python geralmente é melhor do que a implementação manual de Merge Sort por vários motivos:

### Razões pelas quais `sorted()` é preferível:

1. **Eficiência**:
   - **`sorted()`**: Utiliza o Timsort, que é uma combinação de Merge Sort e Insertion Sort, otimizado para diferentes tipos de dados e padrões de dados. Timsort é muito eficiente na prática, com complexidade O(n log n) no pior caso, e é otimizado para arrays parcialmente ordenados.
   - **Merge Sort**: Enquanto Merge Sort tem uma complexidade de O(n log n), o Timsort pode oferecer um desempenho superior na prática, especialmente para dados reais que podem ter padrões de ordenação parciais.

2. **Simplicidade e Manutenção**:
   - **`sorted()`**: É extremamente simples de usar e entender. Basta uma linha de código para ordenar uma lista, e você não precisa se preocupar com os detalhes da implementação do algoritmo.
   - **Merge Sort**: Requer uma implementação manual, o que envolve escrever código para dividir o array, ordenar sub-arrays recursivamente e mesclar os resultados. Isso pode ser mais complexo e sujeito a erros.

3. **Otimizações Específicas**:
   - **`sorted()`**: Aproveita otimizações específicas para tipos de dados e padrões comuns. O Timsort foi projetado para aproveitar padrões de dados comuns, como segmentos de dados já ordenados, e pode lidar melhor com esses casos.
   - **Merge Sort**: Embora seja eficiente, não possui as mesmas otimizações específicas que o Timsort, o que pode resultar em desempenho inferior em certos casos práticos.

4. **Integração e Suporte**:
   - **`sorted()`**: É uma função integrada do Python, com suporte e otimização contínuos pela equipe de desenvolvimento do Python. Isso significa que é bem testada, eficiente e sempre atualizada.
   - **Merge Sort**: Requer que você escreva e mantenha seu próprio código, o que pode ser uma desvantagem se você estiver procurando por uma solução rápida e confiável.

### Comparação

Se você estiver lidando com dados grandes e variados e precisar de uma solução confiável e eficiente, o `sorted()` é geralmente a melhor escolha. Ele oferece um desempenho muito bom para a maioria dos casos e é fácil de usar.

Por outro lado, entender e implementar Merge Sort pode ser útil para aprendizado e compreensão dos conceitos de algoritmos de ordenação e divide-and-conquer. No entanto, para aplicações práticas e produção, confiar em `sorted()` é a abordagem recomendada devido à sua eficiência e simplicidade.

### Exemplos

Vamos comparar a ordenação usando `sorted()` e Merge Sort com um exemplo simples:

**Usando `sorted()`**:
```python
numeros = [3, 7, 6, -10, 15, 23.5, 55, -13]
ordenados = sorted(numeros)
print("Ordenado com sorted:", ordenados)
```

**Implementação de Merge Sort**:
```python
def merge(left, right):
    resultado = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    return merge(esquerda, direita)

numeros = [3, 7, 6, -10, 15, 23.5, 55, -13]
ordenados = merge_sort(numeros)
print("Ordenado com Merge Sort:", ordenados)
```

Ambos os métodos vão resultar na lista ordenada, mas `sorted()` é mais direto e geralmente mais eficiente na prática.
'''