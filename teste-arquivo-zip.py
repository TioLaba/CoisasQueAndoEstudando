# Vamos entender o módulo zip e suas funcionalidades
import zipfile, os  # Importamos os módulos necessários: zipfile para manipular arquivos ZIP e os para interagir com o sistema operacional

# Vamos definir uma função que retorna o caminho principal da área de trabalho
def caminho_principal():
    return 'C:\\Users\\valte\\Desktop'  # Estamos retornando o caminho da área de trabalho onde os arquivos serão manipulados

# Vamos criar uma função para gerar um arquivo txt simples que será compactado em um ZIP
def criar_txt():
    local_arquivo = caminho_principal() + '\\meu-teste-zip.txt'  # Definimos o local onde o arquivo .txt será criado, concatenando com o nome do arquivo
    with open(local_arquivo, 'w') as arquivo:  # Estamos abrindo (ou criando) o arquivo .txt em modo de escrita ('w')
        pass  # O 'pass' aqui significa que o arquivo será criado, mas não escreveremos nada nele por enquanto
    return local_arquivo  # Retornamos o caminho completo do arquivo recém-criado

# Vamos criar uma função para definir o caminho e gerar o arquivo ZIP
def arquivo_zip():
    caminho_zip = caminho_principal() + '\\' + 'arquivo-zip-teste.zip'  # Estamos definindo o caminho onde o arquivo ZIP será criado
    caminho_arquivo = criar_txt()  # Chamamos a função criar_txt para garantir que o arquivo .txt seja criado antes de ser compactado
    with zipfile.ZipFile(caminho_zip, 'w') as arquivo_zip:  # Abrimos o arquivo ZIP em modo de escrita ('w') para começar a adicionar arquivos
        arquivo_zip.write(caminho_arquivo, os.path.basename(caminho_arquivo))  # Adicionamos o arquivo .txt ao ZIP, sem incluir o caminho completo, apenas o nome
    return caminho_zip  # Retornamos o caminho completo do arquivo ZIP criado

# Vamos criar uma função para exibir uma mensagem confirmando a criação do arquivo ZIP
def exibir_arquivo_zip():
    return f'Arquivo ZIP criado com sucesso: {arquivo_zip()}'  # Exibimos uma mensagem de sucesso com o caminho do arquivo ZIP gerado

# Chamamos a função que exibe a mensagem para rodar o processo todo e verificar o sucesso
print(exibir_arquivo_zip())  # Esta linha executa o código e imprime o resultado da função exibir_arquivo_zip()

# podemos listar todos os arquivos em uma pasta ZIP
def listar_arquivos_zip(caminho_do_zip):
    # vamos usar with com metodo 'r' apenas para leitura
    with zipfile.ZipFile(caminho_do_zip, 'r') as arquivo_zip:
        arquivos_listados = arquivo_zip.namelist()
    
    return arquivos_listados

caminho_zip_criado = arquivo_zip()
print(f'Esses são os arquivos contidos na pasta ZIP: ', listar_arquivos_zip(caminho_zip_criado))

# tambem podemos extrair os arquivos dentro da pasta ZIP
def extrair_arquivos_da_pasta_zip(caminho_zip):
    # precisamos definir um destino para extração
    destino_extracao = 'C:\\Users\\valte\\Desktop\\arquivos-extraido-do-zip'
    # vamos criar a pasta para que o destino exista :)
    os.mkdir(destino_extracao)
    # agora sim podemos extrair os arquivos sem problemas 
    with zipfile.ZipFile(caminho_zip, 'r') as arquivo_zip:
        arquivo_zip.extractall(destino_extracao)
    
    # podemos verificar se os arquivos foram extraidos com o caminho que passamos
    return destino_extracao

print(f'OS arquivos foram extraidos nessa pasta: {extrair_arquivos_da_pasta_zip(caminho_zip_criado)}')

