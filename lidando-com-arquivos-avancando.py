import os

# definindo a area de trabalho como caminho
caminho = "C:\\Users\\valte\\Desktop"
caminho_arquivo = "C:\\Users\\valte\\Desktop\\Dev-C++.lnk"

# podemos obter o tamanho de eum arquivo em bytes
print(f'\nO arquivo tem {os.path.getsize(caminho_arquivo)} bytes.')

# tambem podemos receber uma lista de strings com os nomes de arquivo dentro do argumento
print('\nEssa pasta tem esses arquivos: ', os.listdir(caminho))

# podemos conseguir o nome dos arquivos e o tamanho de cada item com uma visualizaçao mais elegante
print() # apenas para quebrar a linha 
tamanho_da_desktop = 0
for nome_arquivo in os.listdir(caminho):
    try:
        # Criando o caminho completo para o arquivo
        caminho_completo = os.path.join(caminho, nome_arquivo)

        # Verificar se é um arquivo antes de obter o tamanho
        if os.path.isfile(caminho_completo):
            tamanho_da_desktop += os.path.getsize(caminho_completo)
            print(f'Nome: {nome_arquivo}  Tamanho:  {os.path.getsize(caminho_completo)}')
    except FileNotFoundError:
        continue

print(f'Tamanho total dos arquivos na desktop: {tamanho_da_desktop} bytes')


# tambem podemos verificar se o caminho passado é uma pasta ou arquivo
# como no exemplo acima verificamos se é um arquivo 
# Desktop é um arquivo ou uma pasta?
if os.path.isdir(caminho):
    print('\nO caminho é uma pasta')
else:
    print('\nO caminho é um arquivo')

# podemos verificar se temos um dvd ou pendrive na maquina
if os.path.exists('D:\\\\'):
    print('\nNão temos pendrive, nem dvd, ou algo do tipo conectado')
else:
    print('Temos algo conectado no computador')

