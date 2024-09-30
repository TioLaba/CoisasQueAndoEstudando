import os, shutil, zipfile


CAMINHO = 'C:\\'

def buscar_pdfs(caminho):
    lista_de_pdfs = []

    for raiz, pastas, arquivos in os.walk(caminho):
        for arquivo in arquivos:

            caminho_do_arquivo = os.path.join(raiz, arquivo)

            _, extensao = os.path.splitext(caminho_do_arquivo)    
            if extensao.lower() == '.pdf':
                # print(f'\nPDF encontrado: {caminho_do_arquivo}')
                lista_de_pdfs.append(caminho_do_arquivo)

    return lista_de_pdfs

pdfs_encontrados = buscar_pdfs(CAMINHO)

def copiar_pdfs(lista_pdf):
    
    # vamos definir aonde vão ser copiado os pdf
    destino = 'C:\\Users\\valte\\Desktop\\todos-meus-pdfs'
    # vamos criar uma pasta para copiar os arquivos em uma pasta do desktop
    os.mkdir(destino)

    for pdf in lista_pdf:
        try:
            shutil.copy2(pdf, destino)
            print('PDF copiado')
        except Exception as erro:
            print(f'Erro : {erro}')

    return destino
copias = copiar_pdfs(pdfs_encontrados)

# Agora vamos zipar a pasta copiada
def zipar_pasta(pasta):
    caminho_do_zip = 'C:\\Users\\valte\\Desktop\\todos-meus-pdfs.zip'
    
    # Criar um arquivo ZIP e adicionar a pasta inteira
    with zipfile.ZipFile(caminho_do_zip, 'w') as arquivo_zip:
        # Adiciona toda a pasta ao zip
        for root, dirs, files in os.walk(pasta):
            for file in files:
                caminho_completo = os.path.join(root, file)
                # Adiciona o arquivo ao zip com a estrutura de diretórios
                arquivo_zip.write(caminho_completo, os.path.relpath(caminho_completo, pasta))
    
    return caminho_do_zip

zipar_pasta(copias)
print('Backup concluido com sucesso')