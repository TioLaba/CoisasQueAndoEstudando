import string
import random

# vamos definir o tamanho da senha
tamanho_da_senha = int(input('Quantos caracteres deve ter a senha?  '))

def gerar_senha(tamanho=8):
    # vamos definir o tipo de caracteres
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # vamos usar uma comprensão basica para selecionar as letras de forma aleatoria
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

print(f'Senha gerada: {gerar_senha(tamanho_da_senha)}')