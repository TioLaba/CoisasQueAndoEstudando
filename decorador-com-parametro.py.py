def decorador(func):
    print('Decorando função')

    def aninhada(*args, **kwargs):
        print('Função aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada

@decorador
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

