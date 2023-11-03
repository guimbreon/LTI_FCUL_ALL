"""
Problema 3:
Escreva uma função que devolva o maior de três números inteiros (deve incluir o 
contrato na escrita). Recorra à função implementada no exercício anterior. Teste a 
função escrevendo um programa que receba três números inteiros do utilizador e
imprima o resultado da chamada à função desenvolvida.
"""
def maior(num1, num2, num3):
    """
    Recebe dois numeros inteiros e devolve o maior deles
    
    Requires: num1, num2, num3 int
    Ensures: o maior entre os numeros dados
    """
    
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num2 and num3 > num1:
        return num3
    
    

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
print(maior(num1,num2,num3))

