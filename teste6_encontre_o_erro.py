'''
6. **Problema: Encontre o Erro**
   - O código abaixo contém um erro lógico. Identifique o erro e corrija-o.
   - **Código:**
     ```python
     def find_largest(nums):
         largest = 0
         for num in nums:
             if num > largest:
                 largest = num
         return largest

     nums = [-5, -1, -3, -4]
     print(find_largest(nums))  # O código deveria retornar -1, mas retorna 0.
     ```
'''

def find_largest(nums):
    largest = nums[0] # 0 deve ser o primeiro elemento da lista e não zero
    # o erro esta aqui, esse codigo busca o menor valor de uma lista, 
    # ele deveria comparar o 1° elemento da lista 
    for num in nums:
        if num > largest:
            largest = num
    return largest # o return se encontrava dentro do loop for o que sempre finalizaria o loop na primeira ocorrencia

nums = [-5, -1, -3, -4]
print(find_largest(nums))  # O código deveria retornar -1, mas retorna 0.