"""
Problema 22: Escreva um programa com a função swapMaxMin(l), que recebe uma lista l de
inteiros e a altera da seguinte forma: o maior e o menor elemento trocam de
posições. Nesse programa adicione interação com o utilizador de forma a testar
essa função
"""
import copy
def swapMaxMin(l):
    maior = copy.deepcopy(l)
    maior.sort()
    menor = maior[0]
    maior = maior[-1]
    l[l.index(menor)],l[l.index(maior)] = maior,menor
    return l

l = [2394,2342,3255,22,4,69]
print(swapMaxMin(l))
