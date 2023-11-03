"""
Problema 6:
Escreva uma função que acrescente um 0 no final de um número inteiro. Por
exemplo, aumenta(73) devolve 730 (se esquecer o contrato a definição da função
está incompleta). aumenta(0) deve devolver 0. Teste a função escrevendo um
programa que receba um número inteiro do utilizador e imprima o resultado da
chamada à função desenvolvida.
"""

def aumenta(num):
    """
    Acrescenta um 0 no final de um número inteiro
    Requires: Um número inteiro
    Ensures: O mesmo número com um 0 no fim.
    """
    return str(num) + "0"
