"""
Problema 7:

Escreva uma função que verifique se um dado número inteiro é uma capicua
usando as funções desenvolvidas nos três exercícios anteriores. Teste a função
escrevendo um programa que receba um número inteiro do utilizador e imprima o
resultado da chamada à função desenvolvida.

"""

def unidades(num):
    """
    Devolve o dígito na csa das unidades de um número inteiro.
    Requires: Número inteiro
    Ensures: Algarismo na casa das unidades do mesmo.    
    """
    return str(num)[-1]

def aumenta(num):
    """
    Acrescenta um 0 no final de um número inteiro
    Requires: Um número inteiro
    Ensures: O mesmo número com um 0 no fim.
    """
    return str(num) + "0"

def retira(num):
    """
    Remove o algarismo das unidades.
    Requires: Número inteiro
    Ensures: o mesmo número, sem o algarismo das unidades.
    """
    num = str(num)
    if len(num) > 1:
        return num[:-1]
    else:
        return 0

def capicua(num):
    i = 0
    outro = 0
    dec = 1
    while len(str(outro)) != len(str(num)):
        print(outro, num)
        outro += int(unidades(num))*dec
        num = int(retira(num))
        dec *= 10
        i += 1
    print(str(outro)[:-1])
    if str(num) == str(outro)[-1:]:
        return True
    else:
        return False
print(capicua(123321))