def receber_texto():
    return input('Digite qualquer texto: ')

def separar_texto(texto):
    return len(texto.split())

if __name__ == '__main__':
    texto = receber_texto()
    quantidade_palavras = separar_texto(texto)
    print(f'O texto fornecido tem {quantidade_palavras} palavras')