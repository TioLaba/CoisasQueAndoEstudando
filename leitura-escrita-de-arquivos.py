# Podemos abrir arquivos com a função open()
abrir_arquivo = open('C:\\Users\\valte\\Desktop\\Python\\livro - automatizar tarefas massantes com python\\parte I - basico da programação python\\hello-word-teste-arquivo.py')

# Podemos ler arquivos com a função read()
ler_arquivo = abrir_arquivo.read()

# Exibindo a leitura do arquivo
print(ler_arquivo)
print()

# Fechando arquivo para evitar bugs
abrir_arquivo.close()  # Correção adicionada: fechar o arquivo depois de ler

# Também podemos obter uma lista de valores de string do arquivo
abrir_texto = open('C:\\Users\\valte\\Desktop\\Python\\livro - automatizar tarefas massantes com python\\parte I - basico da programação python\\texto-qualquer.txt')

# Exibindo todas as linhas em uma lista
ler_linhas_do_arquivo = abrir_texto.readlines()
print(ler_linhas_do_arquivo)
print()

# Fechando arquivo para evitar bugs
abrir_texto.close()  # Correção adicionada: fechar o arquivo depois de ler

# Podemos escrever no arquivo usando 'a' como argumento (adiciona no final do arquivo)
escrevendo_no_texto = open('C:\\Users\\valte\\Desktop\\Python\\livro - automatizar tarefas massantes com python\\parte I - basico da programação python\\texto-qualquer.txt', 'a')
escrevendo_no_texto.write('salve jorge\n')
escrevendo_no_texto.close()  # Fechar o arquivo após a escrita

# Confirmando a escrita - abrindo o arquivo em modo leitura para visualizar o conteúdo
escrevendo_no_texto = open('C:\\Users\\valte\\Desktop\\Python\\livro - automatizar tarefas massantes com python\\parte I - basico da programação python\\texto-qualquer.txt', 'r')
lendo_texto_novo = escrevendo_no_texto.readlines()
print(lendo_texto_novo)
escrevendo_no_texto.close()  # Fechar o arquivo após ler
