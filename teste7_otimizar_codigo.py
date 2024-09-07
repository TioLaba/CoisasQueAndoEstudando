'''
7. **Problema: Otimização de Código**
   - Dado o código abaixo, refatore-o para melhorar sua eficiência e clareza. Explique as alterações realizadas.
   - **Código:**
     ```python
     def process_data(data):
         result = []
         for item in data:
             if item not in result:
                 result.append(item)
         return result
     
     data = [1, 2, 2, 3, 4, 3, 5]
     print(process_data(data))  # Output esperado: [1, 2, 3, 4, 5]
     ```

'''

# esse codigo esta eliminando os valores repetidos de uma lista
def processar_dados(dados):
    remover_repetidos = set(dados)
    return sorted(list(remover_repetidos))

data = [1, 2, 2, 3, 4, 3, 5]
print(processar_dados(data))