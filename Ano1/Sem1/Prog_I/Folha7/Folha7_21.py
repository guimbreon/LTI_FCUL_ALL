"""
Problema 21: Escreva um programa com a função append_lists(l1,l2), que recebe duas
listas l1 e l2 e devolve uma nova lista resultado da junção das duas. Nesse
programa adicione interação com o utilizador de forma a testar essa função. Não
se esqueça de testar com listas de listas
"""
import copy
def append_lists(l1,l2):
    l3 = []
    l3.extend(l1)
    l3.extend(l2)
    return l3

l1 = [2394,2342,3255,22,4,69]
l2 = [123,1243,324,13,783,902]
print(append_lists(l1,l2))
