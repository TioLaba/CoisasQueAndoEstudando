'''
4. **Problema: Context Manager Customizado**
   - Implemente um gerenciador de contexto customizado que crie um arquivo temporário, escreva uma string nele, e depois apague o arquivo quando o bloco de contexto for encerrado.
   - **Requisitos:**
     - O gerenciador de contexto deve ser implementado usando classes e o protocolo `__enter__` e `__exit__`.
   - **Exemplo de Uso:**
     ```python
     with TempFileManager("conteúdo temporário") as filename:
         with open(filename, 'r') as f:
             print(f.read())  # Output: "conteúdo temporário"
     ```

'''
import os # para encontrar e remover o arquivo criado
class GerenciadorDeContexto:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.nome_arquivo = 'arquivo_temporario.txt'


    def __enter__(self):
        print('Gerando arquivo temporario.')
        # crie o arquivo e escreva algo
        with open(self.nome_arquivo, 'w') as arquivo:
            arquivo.write(self.conteudo)

        print('Arquivo gerado com Sucesso.\n')
        return self.nome_arquivo # retorna o nome do arquivo 
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('\nApagando arquivo temporario.')
        # apaga o arquivo criado
        if os.path.exists(self.nome_arquivo): # verifica se o arquivo existe
            os.remove(self.nome_arquivo)
        print('Arquivo Apagado com Sucesso.')

# Exemplo de uso
with GerenciadorDeContexto("conteúdo temporário") as filename:
    with open(filename, 'r') as f:
        print(f.read())