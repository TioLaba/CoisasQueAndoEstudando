'''
Esse é um codigo que realmente não me entra na cabeça, minha falta de experiencia em programação me diz 
- Para que vou escrever todas essas linhas, separar dezena centena e etc....
se posso ordenar a lista usando sorted(lista, key= lambda x: x[1], reverse=False)
'''

def ordenacao_radix(lista):
    # Encontrar o maior valor na lista para determinar o número de dígitos que precisamos percorrer
    maior_valor = max(lista)

    # A variável 'exp' (expoente) vai começar em 1, representando a unidade, e será multiplicada por 10
    # a cada iteração para que possamos analisar o próximo dígito (de unidade -> dezenas -> centenas, etc.)
    exp = 1

    # Continuar enquanto o maior valor dividido por 'exp' for maior que 0.
    # Isso garante que percorremos todos os dígitos do maior número.
    while maior_valor // exp > 0:
        # Chamar a função que ordena a lista com base no dígito atual
        ordenar_com_digito(lista, exp)

        # Multiplicar 'exp' por 10 para passar para o próximo dígito (de unidade para dezena, etc.)
        exp *= 10

def ordenar_com_digito(lista, exp):
    # Criar uma lista de contagem com 10 'baldes', um para cada dígito (0 a 9).
    # Estes 'baldes' vão armazenar temporariamente os números com base no dígito que estamos analisando.
    baldes = [[] for _ in range(10)]

    # Iterar sobre cada número na lista original
    for numero in lista:
        # Calcular qual dígito está na posição atual (exp) que estamos focando.
        # (numero // exp) % 10 pega o dígito do número correspondente à posição atual.
        digito = (numero // exp) % 10

        # Colocar o número no 'balde' correspondente ao dígito atual.
        baldes[digito].append(numero)

    # Limpar a lista original e reinserir os números na ordem dos baldes.
    lista.clear()

    # Recolocar todos os números dos baldes de volta na lista original na ordem correta.
    for balde in baldes:
        lista.extend(balde)

# Exemplo de uso
if __name__ == '__main__':
    # Lista de exemplo para ser ordenada
    lista = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista original:", lista)

    # Chamar a função de ordenação radix
    ordenacao_radix(lista)
    
    # Exibir a lista ordenada
    print("Lista ordenada:", lista)
