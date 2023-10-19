"""
Problema 1:

1. Escreva um programa em Python que peça ao utilizador um número inteiro e
escreva no ecrã o seu quadrado, e que depois de o fazer, o volte a fazer.

i = 0
while i < 2:
    number = int(input("Digite um numero:"))
    print(number**2)

"""
"""
Problema 2:

Escreva um programa em Python que peça ao utilizador um número decimal e 
escreva no ecrã a sua parte inteira perguntando em seguida se o utilizador quer 
terminar a utilização do programa


continuar = True


while continuar:
    numero = float(input("Digite um numero decimal: "))
    print(int(numero))
    pergunta = input("Quer continuar?\nS ou N\n>")
    if pergunta == "N":
        continuar = False
   
"""

"""
Problema 3:
 Escreva um programa em Python que peça ao utilizador um número inteiro n e
escreva no ecrã os números inteiros de 0 a n, um por linha.

i = 0
n = int(input("Digite um número: "))
while i <= n:
    print(i)
    i+=1

"""

"""
Problema 4:
Escreva um programa em Python que peça ao utilizador um número inteiro n e 
escreva no ecrã todas as potências de 2 com expoentes entre 0 e n, uma por linha.
numero = int(input("Digite um número inteiro: "))

i = 0
while i <= numero:
    print(2**i)
    i+= 1

"""
"""
Problema 5:

Escreva um programa em Python que peça ao utilizador um número inteiro k e
uma palavra w e escreva no ecrã k linhas em que cada linha i tem o número da
linha i separado por um espaço da palavra w concatenada i vezes, com i no
intervalo de 1 a k.

i = 0
k = int(input("Digite um numero: "))
w = input("Diga uma palavra: ")
while i <= k:
    print(i, w*i)
    i += 1
"""
"""
Problema 6:
Escreva um programa em Python que peça ao utilizador um número inteiro n e
escreva no ecrã todas as potências de 2 entre 0 e n, uma por linha.


i = 0
k = int(input("Digite um numero: "))
while i <= k:
    print(i**i)
    i += 1
""" 

"""
Problema 7:

Escreva um programa em Python que peça ao utilizador um número inteiro k e
escreva no ecrã o resultado do somatório dos primeiros k inteiros.

i = 0
soma = 0
k = int(input("Digite um numero: "))
while i <= k:
    soma += i
    i += 1
print(soma)
"""

"""
Problema 8:

Escreva um programa em Python que peça ao utilizador um número inteiro k e 
escreva no ecrã o resultado do piatório das potências de 3 com expoente de 0 a k.


k = int(input("Digite um número inteiro: "))
piatorio = 1
i = 0

while i <= k:
    piatorio *= 3**i
    i += 1
print(piatorio)


"""

"""
Problema 9:
Escreva um programa em Python que peça ao utilizador um número inteiro k e
escreva no ecrã o número de múltiplos de 3 no intervalo de 0 a k.

k = int(input("Digite um número inteiro: "))
total = 0
i = 0

while i <= k:
    if i%3 == 0:
        total += 1
    i += 1
print(total)
"""

"""
Problema 10:

Escreva um programa em Python que peça ao utilizador um número inteiro k e 
escreva no ecrã o número de ímpares no intervalo de 0 a k.

k = int(input("Digite um número inteiro: "))

i = 0
soma = 0
while i <= k:
    if i%2 != 0:
        soma += 1
    i += 1
print(soma)

"""
"""
Problema 11:
O João encontra-se no quinto degrau de uma escadaria (a contar de baixo) e
começa a subir os degraus dois a dois. A Joana encontra-se no vigésimo degrau da
mesma escadaria e ao mesmo tempo começa a descer os degraus um a um.
Escreva um programa em Python que diga em que degrau se encontra cada um
deles imediatamente antes de se encontrarem/cruzarem, e que indique também se
eles se vão encontrar no mesmo degrau. Altere o programa de forma a que seja o
utilizador a indicar quais os degraus de partida de ambos

joana = int(input("Em que degrau a joana está? \n>>>"))
joao = int(input("Em que degrau a joao está? \n>>>"))
while joana > joao+2:    
    joana -=1
    joao+=2

print("Antes de se cruzarem:")
print("Joana:",joana,"João:",joao)

if joana == joao
    print("Estão no mesmo degrau!")
"""
"""
Problema 12:

Escreva um programa em Python que que peça ao utilizador um número inteiro
k e escreva a soma dos seus divisores próprios. Um divisor é próprio se for
diferente do número e da unidade. Por exemplo a soma dos divisores próprios de
12 é 2 + 3 + 4 + 6 = 15.

k = int(input("Digite K:\n>>>"))
soma = 0
i = 2
while( k > i):
    if k%i == 0:
        soma += i
    
    i += 1
print(soma)
"""
"""
Problema 13:
Designa-se por números perfeitos os números que são iguais à soma dos seus
divisores próprios mais um. Escreva um programa em Python que peça ao
utilizador um número inteiro k e escreva no ecrã se k é perfeito. Por exemplo, 496
é perfeito porque é igual à soma dos seus divisores próprios (2; 4; 8; 16; 31; 62;
124; 248) mais 1.
k = int(input("Digite K:\n>>>"))

soma = 1 #por começar em 1 nao preciso dar +1
i = 2
while k > i:
    if k%i == 0:
        soma += i
    
    i += 1
if soma == k:
    print("Perfeito")
"""

"""
Problema 14:

Escreva um programa em Python que que peça ao utilizador um número inteiro
k e escreva no ecrã o número de vezes que se consegue dividir k por 2. Note que
este valor corresponde à parte inteira do logaritmo de k na base 2.

k = int(input("Digite k:\n>>>"))
total = 0

while k > 0:
    print(k)
    k //= 2
    total += 1
print(total)
"""
"""
Problema 15:
Escreva um programa em Python que que peça ao utilizador um número inteiro
k maior do que 2 e escreva no ecrã quantos números perfeitos existem entre 2 e k
(inclusive). Por exemplo, existem 4 números perfeitos entre 2 e 10000 (o 6, o 28, o
496 e o 8128).

k = int(input("digite k: "))
total = 0
number = 0
while k > number:
    soma = 1 #por começar em 1 nao preciso dar +1
    i = 2
    while number > i:
        if number%i == 0:
            soma += i
        
        i += 1
    if soma == number:
        print("Perfeito",number)
        total += 1
    number += 1

print(total)
"""
"""
Problema 16:
Escreva um programa em Python que que peça ao utilizador um número inteiro
k e escreva no ecrã se k é ou não um cubo perfeito.

Continuar = True
isIt = False
k = int(input("Digite um numero: "))
i = 0
while i < k and Continuar:
    if i**3 == k:
        Continuar = False
        isIt = True
    i += 1
if isIt:
    print("É cubo perfeito")
else:
    print("Não é")
"""
"""
Problema 17:

Designa-se por número primo um número maior do que 1 que não tem 
divisores próprios. Escreva um programa em Python que que peça ao utilizador um 
número inteiro k e que escreva no ecrã se k é primo. Por exemplo, 2, 3, 5, 7 e 
7919 são números primos


k = int(input("Digite um numero inteiro: "))
i = 2
primo = True
while i < k and primo:
    if k%i == 0:
        primo = False
    i += 1

if primo:
    print("É primo")
else:
    print("Não é primo")


"""

"""
Problema 18:

Escreva um programa em Python que “adivinhe” o número inteiro entre 0 e
100 em que o utilizador está a pensar, através de uma sucessão de tentativas às
quais o utilizador deve responder maior (ou +), menor (ou -) ou certo. Exemplo de
interação com o computador (em itálico os dados introduzidos pelo utilizador):
Pense num número inteiro entre 0 e 100. <enter/return>
O número é 50.
maior
O número é 76.
menor
O número é 63.
enor
Resposta inválida.
O número é 63.
-
O número é 57.
+
O número é 60.
certo

numero_user = int(input("Digite um numero: \n>>>"))
numero = 0
while numero != numero_user:
    print(numero)
    Qual = input("maior ou menor?\n>>>")
    if Qual.lower() == "maior":
        numero += 1
    elif Qual.lower() == "menor":
        numero -=1
    else:
        print("Resposta errado")
"""
"""
Problema 19:
Escreva um programa em Python que que peça ao utilizador um número inteiro
k maior do que 2 e escreva no ecrã quantos números primos existem entre 2 e k
(inclusivé). Por exemplo, existem 1000 números primos entre 2 e 7919.

k = int(input("Digite um numero: \n"))
if k < 2:
    print("O numero inserido é menor que 2.")
else:
    total = 0
    Primo = True
    i = 2
    j = 2
    while i <= k:
        while j < i:
            if i%j == 0:
                Primo = False
            j += 1
        if Primo:
            total += 1
        Primo = True
        j = 2
        i += 1
print(total)
"""
"""
Problema 20: 
Escreva um programa em Python que peça ao utilizador um número inteiro k
maior do que 10 e escreva no ecrã quantas capícuas existem entre 10 e k. Uma
capícua é um número que se lê de igual forma da esquerda para a direita e da
direita para a esquerda. Por exemplo, entre 10 e 100 existem 9 capícuas.


k = int(input("Digite um numero: \n"))
i= 10
j = 0
total = 0
if k > 10:
    Validado = 0
    while i <= k:
        MetTamanho = len(str(i))/2
        while j <= MetTamanho:
            if str(i)[j] == str(i)[-(j+1)]:
                Validado += 1
            j += 1
        if Validado == len(str(i)):
            total += 1
        j = 0
        Validado = 0
        i += 1
else:
    print("O numero tem que ser maior que 10.")
print(total)
"""