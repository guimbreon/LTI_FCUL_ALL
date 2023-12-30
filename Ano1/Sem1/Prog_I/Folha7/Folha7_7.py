"""
Problema 7:

Escreva um programa com a função get_max(l), que recebe uma lista l de inteiros
e devolve o maior número existente na lista. Nesse programa adicione interação
com o utilizador de forma a testar essa função

"""
import copy
def get_max(l):
    """
    Devolve o maior número de uma determinada lista.
    Requires: list l
    Ensures: o maior dos números
    """
    maior = copy.deepcopy(l)
    maior.sort()
    return maior[-1]

l = [2,31,21,1313,0]

print(get_max(l))
