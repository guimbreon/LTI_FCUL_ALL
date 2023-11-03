"""
Problema 11:

Usando a função do exercício anterior, escreva um programa que receba um 
número inteiro n maior do que 2 e escreva no ecrã quantos números primos 
existem entre 2 e n (inclusive). Por exemplo, existem 1000 números primos entre 2 
e 7919. Teste a função escrevendo um programa que receba um número inteiro do 
utilizador e imprima o resultado de chamada à função desenvolvida. Explique, nesta 
situação, em que difere a programação defensiva da programação por contratos


"""

def primo(num):
    """
    Verifica se uym dado numero é primo ou não
    
    Requires: num INT num > 1
    Ensures: um boolean com o valor True, se for primo e um boolean com o valor False se não for primo
    """

    i = 2
    Primo = True
    while i < num and Primo:
        if num%i == 0:
            Primo = False
        i += 1
    return Primo

def quantPrimos(num):
    """
    Verifica quantos numeros primos existem entre 2 e num(inclusive).
    
    Requires: num int
    Ensures: total int -> numero total de numeros primos entre 2 e num\.
    """
    
    total = 0
    i = 2
    while i <= num:
        if primo(i):
            total +=1
        i += 1
    
    return total

print(quantPrimos(7919))
