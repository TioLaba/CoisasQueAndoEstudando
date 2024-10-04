import requests  # Importa o módulo requests para fazer requisições HTTP
from PIL import Image  # Importa o módulo PIL para manipulação de imagens
from io import BytesIO  # Importa BytesIO para manipulação de dados de imagem em memória
from bs4 import BeautifulSoup  # Importa BeautifulSoup para análise de HTML

# Passo 1: Faz a requisição HTTP ao site da Google
url = 'https://www.google.com'  # Define o URL da página da Google
response = requests.get(url)  # Faz uma requisição GET para obter o conteúdo HTML da página

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:  # Verifica se o código de status HTTP é 200 (sucesso)
    html_content = response.text  # Armazena o conteúdo HTML da resposta
    soup = BeautifulSoup(html_content, 'html.parser')  # Analisa o HTML usando BeautifulSoup

    # Passo 2: Encontra a tag <img> correspondente ao logo da Google
    logo_img = soup.find('img', alt='Google')  # Busca a tag <img> com o atributo alt='Google'
    
    if logo_img:  # Verifica se a imagem foi encontrada
        # Obtém o URL da imagem
        logo_url = logo_img['src']  # Extrai o valor do atributo 'src' da tag <img>

        # Passo 3: Faz a requisição para o URL da imagem
        if logo_url.startswith('/'):  # Verifica se o URL da imagem é relativo
            logo_url = 'https://www.google.com' + logo_url  # Concatena o URL base para formar o URL completo
        
        img_response = requests.get(logo_url)  # Faz uma requisição GET para o URL da imagem
        
        # Verifica se a requisição da imagem foi bem-sucedida
        if img_response.status_code == 200:  # Verifica se o código de status HTTP é 200 (sucesso)
            # Passo 4: Abre a imagem no Python usando Pillow
            img_data = img_response.content  # Armazena o conteúdo binário da imagem
            img = Image.open(BytesIO(img_data))  # Carrega a imagem em memória usando BytesIO
            
            # Exibe a imagem
            img.show()  # Abre a imagem usando o visualizador de imagens do sistema
        else:
            print(f"Erro ao baixar a imagem. Status code: {img_response.status_code}")  # Exibe erro caso a requisição da imagem falhe
    else:
        print("Logo da Google não encontrado.")  # Exibe uma mensagem se a imagem do logo não for encontrada
else:
    print(f"Erro ao acessar a página. Status code: {response.status_code}")  # Exibe erro caso a requisição da página falhe
