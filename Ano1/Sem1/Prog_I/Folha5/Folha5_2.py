"""
Problema 2:
Escreva uma função que receba dois números inteiros e devolva o maior deles. 
Inclua o contrato da função. Teste a função escrevendo um programa que receba
dois números inteiros do utilizador e imprima o resultado da chamada à função 
desenvolvida. Como teria de fazer para determinar o menor de dois números com 
uma segunda função que tirasse partido de chamar a primeira?

"""

def maior(num1, num2):
    """
    O maior de dois numeros dados.
    
    Requires: num1, num2 int
    Ensures: o maior entre num1 e num2
    """
    
    if num1 > num2:
        return num1
    else:
        return num2 #se for igual ele retorna o num2
    
    
def menor(num1, num2):
    """
    Retorna o menor deles.
    
    Requires: num1,num2 int
    Ensures: o menor entre num1 e num2
    """
    
    if num1 == maior(num1, num2):
        return num2
    else:
        return num1


num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
print(maior(num1,num2))
print(menor(num1,num2))
