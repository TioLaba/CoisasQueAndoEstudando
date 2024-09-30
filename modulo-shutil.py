import os # para criar uma pasta na area de trabalho
import shutil # para manipular arquivos de modo eficiente

# vamos criar uma pasta dentro da area de trabalho com o nome teste-shutil
# Verifica se a pasta já existe para evitar erro
caminho_pasta_nova = "C:\\Users\\valte\\Desktop\\teste-shutil"
if not os.path.exists(caminho_pasta_nova):
    os.mkdir(caminho_pasta_nova)
else:
    print("A pasta já existe na área de trabalho")

# vamos salvar o caminho da pasta criada
# Nota: Como a pasta já existe, o código seguirá normalmente

# vamos definir um destino para a função copia do modulo shutil
destino_nova_pasta_copia = 'C:\\Users\\valte\\Desktop\\Python\\livro - automatizar tarefas massantes com python\\parte I - basico da programação python\\teste-shutil'

# usamos a função copytree para copiar a pasta da area de trabalho para a pasta de programas em python
# Adiciona verificação para evitar erro se a pasta de destino já existir
if not os.path.exists(destino_nova_pasta_copia):
    shutil.copytree(caminho_pasta_nova, destino_nova_pasta_copia)
else:
    print('A pasta de destino já existe, não será copiada novamente.')

# podemos verificar se a pasta foi copiada com sucesso usando path.exists
if os.path.exists(destino_nova_pasta_copia):
    print('Copia Bem sucedida')
else:
    print('Houve algum erro')

# podemos mover a pasta que foi copiada novamente para o desktop
# vale lembrar que se os arquivos tiverem o mesmo destino, shutil.move renomeia os arquivos ao inves de mover
# Verifica se já existe uma pasta com o mesmo nome no destino
if not os.path.exists('C:\\Users\\valte\\Desktop\\teste-shutil'):
    shutil.move(destino_nova_pasta_copia, 'C:\\Users\\valte\\Desktop')
    print("Movemos a pasta para o Desktop")
else:
    print("A pasta já existe no Desktop, não será movida.")

# podemos verificar se a pasta foi movida para o desktop com codigo
# 1° vamos armazenar todos os items da desktop em uma lista
desktop = os.listdir('C:\\Users\\valte\\Desktop')

# agora perguntamos se a pasta teste-shutil se encontra no desktop
if 'teste-shutil' in desktop:
    print('Movemos a pasta copiada com sucesso para o Desktop')
else:
    print('Houve algum erro verifique')

# podemos apagar arquivos com os.unlink dentro de alguma pasta
# podemos apagar pastas vazias com os.rmdir dentro de algum caminho fornecido
# podemos apagar pastas inteiras com shutil.rmtree dentro de algum caminho fornecido

''' vamos testar os pequenos conhecimentos adquiridos '''

# vamos criar um loop para criar 10 arquivos txt
for arquivo_txt in range(10):
    # vamos usar with open me parece mais legivel
    caminho_arquivo = f'C:\\Users\\valte\\Desktop\\teste-shutil\\arquivo_{arquivo_txt}.txt'
    with open(caminho_arquivo, 'w') as teste:
        teste.write(f'Esse arquivo é o arquivo: {arquivo_txt}')
    
    # vamos verificar se foi criado com sucesso
    if os.path.exists(caminho_arquivo):
        print(f'Arquivo {caminho_arquivo} criado com sucesso')
    else:
        print(f'Erro ao criar o arquivo {caminho_arquivo}')

    