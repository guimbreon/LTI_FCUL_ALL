"""
Problema 4:

Escreva uma função unidades (escrever o contrato faz parte da escrita da
função) que devolva o dígito na casa das unidades de um número inteiro. Por
exemplo unidades(43) deve devolver 3. Teste a função escrevendo um programa
que receba um número inteiro do utilizador e imprima o resultado de chamada à
função desenvolvida.
"""
def unidades(num):
    """
    Devolve o dígito na csa das unidades de um número inteiro.
    Requires: Número inteiro
    Ensures: Algarismo na casa das unidades do mesmo.    
    """
    return str(num)[-1]
