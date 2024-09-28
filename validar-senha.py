import re

senha = "@Vs44611644"
# senha deve ter letras minúsculas, maiúsculas, números, símbolos e no mínimo 8 caracteres
def validar_senha(senha):
    regex = [r'[A-Z]', r'[a-z]', r'\d', r'[!@#$%¨&*()_\-+=]']

    # verificando se a senha atende a todos os critérios
    if all(re.search(x, senha) for x in regex):
        return True
    else:
        return False
    
def verificar_tamanho(senha):
    return len(senha) >= 8
    
if __name__ == '__main__':
    if verificar_tamanho(senha) and validar_senha(senha):
        print("Senha Aprovada")
    else:
        print("Senha recusada, tente novamente")
