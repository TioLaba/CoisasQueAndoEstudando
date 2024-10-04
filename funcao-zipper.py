import itertools
lista = [x * 2 for x in range(10)]
lista1 = [x * 3 for x in range(10)]

nova_lista = list(zip(lista, lista1))
# print(nova_lista)

lista2 = [1, 2, 3, 4, 5, 6]
lista3 = [1, 2, 3, 4,]

menor_lista = min(len(lista2), len(lista3))
somar = [lista2[x] + lista3[x] for x in range(menor_lista)]
print(somar)


lista_combinar = itertools.permutations(lista2)
add_permutacao = []
for x in lista_combinar:
    add_permutacao.append(list(x))
    print(list(x))


print('itens gerados : ',len(add_permutacao))