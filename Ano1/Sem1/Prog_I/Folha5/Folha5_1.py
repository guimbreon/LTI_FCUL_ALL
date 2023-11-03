"""
Problema 1:
Escreva uma função com nome succ que receba um número inteiro e devolva o
inteiro seguinte, i.e., o sucessor do número dado. Escreva o contrato da função
usando uma docstring: não esquecer de incluir a descrição da função, a descrição e
tipo do parâmetro e a descrição e o tipo do valor que a função devolve. Teste a
função incluindo no seu programa o comando de impressão do resultado da
chamada à função succ(-1). Experimente fazer help(succ) no modo interativo do
interpretador Python.
"""

def succ(num):
    """
    Develve o número inteiro seguinte.
    Requires: num INT
    Ensures: o próximo número.
    """
    return num+1