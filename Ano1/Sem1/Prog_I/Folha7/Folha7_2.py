"""
2) Escreva um programa com a função tdiv em linguagem Python que receba um
número inteiro positivo e devolva um tuplo com os seus divisores. Nesse programa
adicione interacção com o utilizador de forma a testar essa função.
"""
import copy
def tdiv(num):
    divisores = ()
    i = 1
    while i < num:
        if num%i == 0:
            divisores += (i,)
        i += 1
    return divisores

print(tdiv(25))
