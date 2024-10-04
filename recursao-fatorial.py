# aumentando limite da recursão
import sys

sys.setrecursionlimit(1500) # a recursão tem um limite 

def recursiva(inicio=1, fim=10):
    # criamos um caso base para finalizar a recursão
    if inicio >= fim:
        return fim
    
    # print(inicio) # esta aqui apenas mapear e ver as execuções
    # esse é o caso recursivo
    # vai se repetindo ate o caso base
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva(0, 1498))

def fatorial(n):
    # caso base para fim da recursão
    if n <= 1:
        return 1
    # print(n) # apenas mapeando a recursão
    return n * fatorial(n - 1)

print(fatorial(5))