import os

# obter o diretorio de trabalho atual
dir_tra_atual = os.getcwd()

# Exibir o diretorio de trabalho atual
print(f'Diretorio de Trabalho Atual: {dir_tra_atual}\n')

# podemos ir para qualquer outro ambiente de trabalho (diretorio de trabalho atual)
os.chdir("C:\\Users\\Valte")

# exibindo a mudança de ambiente
print('Mudamos para esse Diretorio: ', os.getcwd())

# vamos voltar ao diretorio de trabalho inicial
os.chdir(dir_tra_atual)

#Exibindo a volta ao ponto inicial
print('\nVoltando para o diretorio inicial: ', os.getcwd())

# podemos criar pastas de forma bem facil
# os.mkdirs("C:\Users\\valte\\Desktop\\pasta-criada-via-os\\mkdirs-criou-varias-pastas")
# os.mkdir("C:\Users\\valte\\Desktop\\pasta-criada-via-os\\mkdir-criou-varias-pastas\\sem-plural-so-uma-pasta")

# definindo a area de trabalho como caminho
caminho = "C:\\Users\\valte\\Desktop\\Dev-C++.lnk"

# paths absolutos - pasta raizes de arquivos

# Exibir path absoluto - abspath
print('\nConverter path relativo em absoluto: ', os.path.abspath(caminho))

# verificar se o path é absoluto
print('\nO path é absoluto: ', os.path.isabs("C:\\Users\\valte\\Desktop\\Dev-C++.lnk"))

# caminho absoluto real
print('\nO caminho absoluto real: ', os.path.realpath(caminho))

# Nome base - nome do arquivo
print('\nO Nome base : ', os.path.basename(caminho))

# dirname(caminho) retorna tudo que estiver antes da ultima barra no argumento
print('\nNome do Diretorio : ', os.path.dirname(caminho))

# podemos separar o caminho absoluto e relativo com split
print('\nSeparando os nomes : ', os.path.split(caminho))