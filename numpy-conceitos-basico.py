import numpy as np
import re
from random import choice
import string

letras = string.ascii_lowercase
teste_besta = np.array([choice(letras) for x in range(27)])
print(teste_besta, '\nArray de strings: ', teste_besta.dtype)
# iniciando array basico
meu_array= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Checando Array
print('Meu array: ', meu_array)
print('Checando tipo: ', type(meu_array))
print('Checar tipo de dados: ', meu_array.dtype)
print('Checar dimensão: ', meu_array.ndim) # para checar a dimensao, diferente de ndmin

# Iniciando Array 2-D Manualmente
meu_array_2d = np.array(

# Primeira Dimensão

[ # Abrimos Com Colchetes

# Segunda Dimensão

[1, 2, 3], [4, 5, 6] # Um Array Com Exatas Duas listas 

] # Fechamos com Colchetes

)
# Visualizamos o Array
print('Array 2-D:\n', meu_array_2d, '\nFeito Manualmente.')

# Podemos usar o parametro ndmin para criar arrays com as dimensões definidas
meu_array_2d_ndmin = np.array([1, 2, 3, 4, 5], ndmin=2) # Observe que ndmin define as dimensões, enquanto ndim apenas retorna a quantidade de dimensões

# Visualizando o Array com ndmin
print('Ndmin para definir Dimensões: \n', meu_array_2d_ndmin)

# Confirmando as dimensões
if meu_array_2d_ndmin.ndim == 2:
    print("\nComo esperado Duas dimensões: ", meu_array_2d_ndmin.ndim)
else:
    print('\nDeu ruim , quantas dimensões? ', meu_array_2d_ndmin.ndim)


'''
Mini Desafio - criar um array de 0 a 100
filtrar todos os multiplos por 3

usar bubble sort para inverter a ordem do array 100 a 0 apenas com multiplos por 4

'''

array = np.array([x for x in range(100)])
copia_array = array.copy()
filtrar_tres = np.array([x for x in copia_array if x % 3 == 0])

def bubble_sort(lista):
    n = len(lista)
    for i in range(n + 1):
        for a in range(n - i - 1):
            if lista[a] <= lista[a + 1]:
                lista[a], lista[a + 1] = lista[a +1], lista[a]
    return lista

filtrar = np.array([x for x in copia_array.copy() if x % 4 == 0])
ordenado = bubble_sort(filtrar)
print(ordenado)