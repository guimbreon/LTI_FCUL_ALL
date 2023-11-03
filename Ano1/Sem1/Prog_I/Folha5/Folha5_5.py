"""
Problema 5:

Escreva uma função (o contrato não pode ser esquecido) que elimine a casa das
unidades de um número inteiro. Por exemplo, retira(537) devolve 53. Se o
argumento só tiver algarismo das unidades, a função deve devolver 0. Teste a
função escrevendo um programa que receba um número inteiro do utilizador e
imprima o resultado de chamada à função desenvolvida.
"""
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