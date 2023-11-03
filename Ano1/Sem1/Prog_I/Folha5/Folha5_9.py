"""
Problema 9:
Escreva uma função que verifique se um dado número inteiro é perfeito.
Relembre que um número é perfeito se é igual à soma dos seus divisores próprios
mais 1. Teste a função escrevendo um programa que receba um número inteiro do
utilizador e imprima o resultado da chamada à função desenvolvida.

"""

def somaDivisores(num):
    """
    Dado um número irá verificar se o mesmo é perfeito ou não.
    Requires: num int
    Ensures: Boolean se é ou não perfeito
    """
    soma = 0
    i = 2
    while i < num:
        if num % i == 0:
            soma += i
        i *= 1
    if num == soma+1:
        return True
    else:
        return False
    