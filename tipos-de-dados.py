# Introdução às Expressões em Python
# Em Python, 2 + 2 é uma 'expressão', o tipo mais básico de instrução em programação.
# As expressões são formadas por 'valores' (como 2) e 'operadores' (como +). 
# Elas podem ser avaliadas a um único valor, podendo ser usadas em qualquer lugar do código.

# Operadores matemáticos em ordem de precedência
exponencial = 2 ** 3           # Potência
modulo_resto = 22 % 8          # Módulo (resto da divisão)
divisao_inteira = 22 // 8      # Divisão inteira
divisao = 22 / 8                # Divisão normal
multiplicacao = 3 * 5          # Multiplicação
subtracao = 5 - 2              # Subtração
adicao = 2 + 2                  # Adição

# Exemplo de cálculo
calcular = (5 * 3) * (4 / 2) - (57 + 3) + (10 - 3)
# Passo a passo:
# calcular = 15 * 2 - 60 + 7
# calcular = 30 - 53
# calcular = -23
print(calcular)

# Tipos de Dados
# Expressões são combinações de valores e operadores, sempre avaliadas a um único valor.

# Definição de tipos de dados
inteiro = 5                   # Um número inteiro
flutuante = 3.14             # Um número decimal
strings = 'Strings são textos'  # Texto entre aspas

# Concatenando e repetindo strings
# O operador '+' une (concatena) strings
nome = 'Valter '
segundo_nome = 'Sergio'
unir_nomes = nome + segundo_nome
print(unir_nomes)  # Saída: Valter Sergio

# O operador '*' repete a string
linha = '_' * 20  # Cria uma linha de 20 underscores
print(linha)      # Saída: ________________

# Variáveis em Python
# Variáveis são espaços na memória que armazenam valores.
# Usamos '=' para atribuir um valor à variável.
meu_espaco_na_memoria = 'qualquer coisa' + str(50) * 5
print(f"Podemos guardar tudo, desde funções complexas a simples números: {meu_espaco_na_memoria}")

# Visualizando o tamanho da variável na memória
import sys
print(f"Essa variável possui {sys.getsizeof(meu_espaco_na_memoria)} bits. Esse valor se refere apenas ao objeto em si, não aos objetos que ele referencia.")

# Exercícios Práticos
# página 66 respostas

#1. Quais das opções a seguir são operadores e quais são valores?
# - > operador
# 'hello' -> valor
# -88.8 -> valor
# - -> operador
# / -> operador
# + -> operador
# 5 -> valor

#2. Qual das opções a seguir é uma variável e qual é uma string?
# spam -> variável
# 'spam' -> string

#3. Nomeie três tipos de dados.
# inteiro = -5
# flutuante = -3.45
# strings = "- Valtinho -"

#4. De que é composta uma expressão? O que fazem as expressões?
# Expressões são compostas por operadores e valores, resolvem cálculos aritméticos.

#5. Este capítulo apresentou as instruções de atribuição, por exemplo, spam = 10. Qual é a diferença entre uma expressão e uma instrução?
# Uma expressão é uma combinação de valores e operadores que resulta em um valor, enquanto uma instrução é um comando que executa uma ação, como atribuir um valor a uma variável.

#6. O que a variável bacon conterá após o código a seguir ser executado?
#bacon = 20
#bacon + 1
# bacon vai possuir o inteiro 20; não foi atribuído 1 na variável bacon.

#7. Para que valores as duas expressões a seguir serão avaliadas?
# 'spam' + 'spamspam' -> concatena as strings
# 'spam' * 3 -> repete a string

#8. Por que eggs é um nome válido de variável enquanto 100 é inválido?
# Por via de regras, o Python não aceita números e símbolos no início de variável.

#9. Quais três funções podem ser usadas para obter uma versão inteira, de ponto flutuante ou em string de um valor?
# int(), float(), str()

#10. Por que a expressão a seguir causa um erro? Como você pode corrigi-la?
# 'I have eaten ' + 99 + ' burritos.'
# Causa erro por causa das aspas antes de 'burritos'. Não se pode concatenar números com string.
# Correção: 'I have eaten ' + str(99) + ' burritos.'