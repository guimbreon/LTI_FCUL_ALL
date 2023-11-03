"""
Problema 10:

Escreva uma função que verifique se um dado número dado é primo. Relembre 
que um número é primo se é maior do que 1 e não tem divisores próprios. Teste a 
função escrevendo um programa que receba um número inteiro do utilizador e 
imprima o resultado da chamada à função desenvolvida

"""
def primo(num):
    """
    Verifica se uym dado numero é primo ou não
    
    Requires: num INT num > 1
    Ensures: um boolean com o valor True, se for primo e um boolean com o valor False se não for primo
    
    """
    i = 2
    prima = True
    while i < num and prima:
        if num%i == 0:
            prima = False
        i += 1
    return prima


print(primo(5))
