'''
2. **Problema: Ordenação de Strings por Frequência de Caracteres**
   - Dada uma lista de strings, ordene as strings em ordem decrescente com base na frequência do caractere mais frequente em cada string. Se duas strings tiverem a mesma frequência máxima, ordene-as lexicograficamente.
   - **Requisitos:**
     - Implemente uma função que recebe uma lista de strings e retorna a lista ordenada conforme descrito.
   - **Exemplo de Entrada:**
     ```python
     strings = ["banana", "apple", "mango", "cherry"]
     ```
   - **Exemplo de Saída:**
     ```python
     ["banana", "apple", "cherry", "mango"]
     ```
   - **Explicação:** A string "banana" tem 'a' com frequência 3, "apple" tem 'p' com frequência 2, "mango" tem 'a' com frequência 1, e "cherry" tem 'r' com frequência 2. Como "banana" tem a maior frequência, ela vem primeiro. "apple" e "cherry" têm a mesma frequência máxima (2), mas "apple" vem antes lexicograficamente.

'''

def ordenar_string(lista_string):
    def ordenar_frequencia(palavra):
        frequencia = {}
        for letra in palavra:
            if letra in frequencia:
                frequencia[letra] += 1
            else:
                frequencia[letra] = 1
        
        return max(frequencia.values())
    
    ordenar_lista = sorted(lista_string, key=lambda palavra: (-ordenar_frequencia(palavra), palavra))
    return ordenar_lista

strings = ['mango', 'cherry', 'apple', 'banana']
ordenar = ordenar_string(strings)
print(ordenar)
