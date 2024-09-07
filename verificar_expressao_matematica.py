'''
def verificar_equacao(equacao):
    abrir = '[{('  # símbolos que representam abertura de expressões (colchetes, chaves, parênteses)
    fechar = ']})'  # símbolos que representam fechamento de expressões

    pilha = []  # lista que atuará como pilha para armazenar os símbolos de abertura

    for caracter in equacao:  # percorre cada caractere da equação
        if caracter in abrir:  # verifica se o caractere atual é um símbolo de abertura
            pilha.append(caracter)  # se for, adiciona o símbolo na pilha
        elif caracter in fechar:  # verifica se o caractere atual é um símbolo de fechamento
            posicao = fechar.index(caracter)  # obtém a posição do símbolo de fechamento
            if len(pilha) > 0 and abrir[posicao] == pilha[-1]:  # se a pilha não está vazia e o topo da pilha corresponde ao fechamento correto
                pilha.pop()  # remove o símbolo de abertura correspondente da pilha
            else:
                return False  # se não houver correspondência ou a pilha estiver vazia, a equação é inválida
    
    return len(pilha) == 0  # se a pilha estiver vazia no final, significa que todas as aberturas foram fechadas corretamente

def analisar_equacoes(lista):
    resposta = []
    enumerar = 0
    for x in lista:
        conta = verificar_equacao(x)
        enumerar += 1
        listar = [f'Questão {enumerar}' ,f'Equação: {x}', f'Esta correta: {conta}']
        resposta.append(listar)
    return resposta


def exibir_resposta(lista):
    for x in lista:
        print(x)
# Lista de equações válidas
# Lista de equações válidas
lista = [
    "x = 3x + (2x * 3) / 2 + (3 - 2) * [5 * 3] ** {34 - 12}",
    "(x + y) * (z + w)",
    "{a + (b * c) / [d - e]}",
    "2 * (3 + 5) - [4 * {6 / (7 - 8)}]",
    "((a + b) * c) - [d / (e + f)]",
    "(3 + 2) * {4 / [6 - (5 * 2)]}",
    "[3 + 2] * (4 - 1) ** {5 / 2}",
    "{(a / b) + [c * d]}",
    "3 + {2 * [1 + (4 / 2)]}",
    "x = {y + [z * (w + t)] / 5}",
    "(a * b) + {c / [d - (e * f)]}",
    "4 * (5 + [6 - {7 * (8 / 2)}])",
    "{(2 + 3) * [4 - (5 / 2)]}",
    "x = 5 + (3 * 4) - {2 / [6 - 1]}",
    "[a + b] - {c / (d * [e + f])}",
    "x = 3x + (2x * 3) / 2 + (3 - 2 * [5 * 3] ** {34 - 12",  # Falta fechar um parêntese
    "(x + y * (z + w",  # Falta fechar um parêntese
    "{a + (b * c) / [d - e]",  # Falta fechar a chave
    "2 * (3 + 5 - [4 * {6 / (7 - 8)}",  # Falta fechar colchete
    "(a + b) * c) - [d / (e + f)]",  # Parêntese extra
    "(3 + 2) * {4 / [6 - (5 * 2)]",  # Falta fechar chave
    "[3 + 2 * (4 - 1] ** {5 / 2}",  # Falta fechar parêntese e colchete
    "{(a / b) + [c * d)",  # Falta fechar colchete
    "3 + {2 * [1 + (4 / 2)]",  # Falta fechar chave
    "x = {y + [z * (w + t] / 5}"  # Falta fechar parêntese
]

# Exibindo as listas
exibir_resposta(analisar_equacoes(lista))
'''

def verificar_equacao(equacao):
    abrir = {'(': ')', '[': ']', '{': '}'}  # Mapeamento de símbolos de abertura para seus fechamentos correspondentes
    pilha = []  # Lista para funcionar como uma pilha

    for caracter in equacao:  # Percorre cada caractere da equação
        if caracter in abrir:  # Se o caractere é um símbolo de abertura
            pilha.append(caracter)  # Adiciona na pilha
        elif caracter in abrir.values():  # Se é um símbolo de fechamento
            if not pilha or abrir[pilha.pop()] != caracter:  # Verifica se o topo da pilha fecha corretamente
                return False  # Equação inválida se não fechar corretamente
    return not pilha  # Se a pilha está vazia, a equação é válida

def analisar_equacoes(lista_equacoes):
    respostas = []
    for indice, equacao in enumerate(lista_equacoes, 1):
        valida = verificar_equacao(equacao)
        resposta_formatada = [f'Questão {indice}', f'Equação: {equacao}', f'É válida: {valida}']
        respostas.append(resposta_formatada)
    return respostas

def exibir_resposta(lista_respostas):
    for resposta in lista_respostas:
        print("\n".join(resposta))  # Junta as linhas da resposta e imprime de uma vez
        print()  # Linha em branco entre as respostas

# Lista de equações válidas e inválidas
lista_equacoes = [
    "x = 3x + (2x * 3) / 2 + (3 - 2) * [5 * 3] ** {34 - 12}",
    "(x + y) * (z + w)",
    "{a + (b * c) / [d - e]}",
    "2 * (3 + 5) - [4 * {6 / (7 - 8)}]",
    "((a + b) * c) - [d / (e + f)]",
    "(3 + 2) * {4 / [6 - (5 * 2)]}",
    "[3 + 2] * (4 - 1) ** {5 / 2}",
    "{(a / b) + [c * d]}",
    "3 + {2 * [1 + (4 / 2)]}",
    "x = {y + [z * (w + t)] / 5}",
    "(a * b) + {c / [d - (e * f)]}",
    "4 * (5 + [6 - {7 * (8 / 2)}])",
    "{(2 + 3) * [4 - (5 / 2)]}",
    "x = 5 + (3 * 4) - {2 / [6 - 1]}",
    "[a + b] - {c / (d * [e + f])}",
    "x = 3x + (2x * 3) / 2 + (3 - 2 * [5 * 3] ** {34 - 12",  # Falta fechar um parêntese
    "(x + y * (z + w",  # Falta fechar um parêntese
    "{a + (b * c) / [d - e]",  # Falta fechar a chave
    "2 * (3 + 5 - [4 * {6 / (7 - 8)}",  # Falta fechar colchete
    "(a + b) * c) - [d / (e + f)]",  # Parêntese extra
    "(3 + 2) * {4 / [6 - (5 * 2)]",  # Falta fechar chave
    "[3 + 2 * (4 - 1] ** {5 / 2}",  # Falta fechar parêntese e colchete
    "{(a / b) + [c * d)",  # Falta fechar colchete
    "3 + {2 * [1 + (4 / 2)]",  # Falta fechar chave
    "x = {y + [z * (w + t] / 5}"  # Falta fechar parêntese
]

from random import shuffle

# Embaralhar a lista
shuffle(lista_equacoes)

# Exibir o resultado das verificações
exibir_resposta(analisar_equacoes(lista_equacoes))