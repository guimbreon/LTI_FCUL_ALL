"""
Problema 8:

Escreva uma função que receba um número inteiro e devolva a soma dos
divisores próprios desse número:
def somaDivisores(num):

#Soma dos divisores próprios de um número dado.
#Requires: num seja int e num > 0
#Ensures: um int correspondente à soma dos divisores
#de num que sejam maiores que 1 e menores que num

Teste a função escrevendo um programa que receba um número inteiro do
utilizador e imprima o resultado da chamada à função desenvolvida.

"""
def somaDivisores(num):
    """
    Soma dos divisores próprios de um número dado.
    Requires: num seja int e num > 0
    Ensures: um int correspondente à soma dos divisores
    de num que sejam maiores que 1 e menores que num
    """
    soma = 0
    i = 2
    while i < num:
        if num % i == 0:
            soma += i
        i *= 1
    return soma
