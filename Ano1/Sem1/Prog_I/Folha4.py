"""
Problema 1:
Escreva um programa que leia um inteiro n e escreva os números pares
existentes entre 0 e n, um por linha. Utilize um ciclo for para o efeito.

n = int(input("Escreva um número"))

for number in range(0,n+1,2):
    print(number)
"""

"""
Problema 2:
Escreva um programa que leia um inteiro n e um inteiro m e escreva os
números entre 0 e n, inclusive, de m em m. Utilize um ciclo for para o efeito.

n = int(input("Escreve um número(n): "))
m = int(input("Escreve um número(m): "))

for i in range(0, n+1, m):
    print(i)
"""

"""
Problema 3:

Escreva um programa que leia um inteiro n e escreva a soma dos números
inteiros entre 0 e n. Utilize um ciclo for para o efeito.

n = int(input("Digite um numero: "))
soma = 0
for i in range(0,n+1):
    soma += i
print(soma)
"""

"""
Problema 4:

Escreva um programa que leia um inteiro n e escreva quantos números pares
existem, entre 0 e n. Utilize um ciclo for para o efeito.

n = int(input("Digite um numero: "))
soma = 0
for i in range(0, n+1, 2):
    soma += i
print(soma)
"""

"""
Problema 5:

Escreva um programa que peça ao utilizador um número inteiro k e escreva no
ecrã o número de múltiplos de 3 que não sejam múltiplos de 2, no intervalo de
0 a k.

k = int(input("Digite um numero: "))
for i in range(0,k+1):
    if i%3 == 0 and i%2 != 0:
        print(i)
"""

"""
Problema 6: 

Escreva um programa que leia um inteiro n e escreva a soma dos números
inteiros ímpares entre 0 e n. Utilize um ciclo for para o efeito.

n = int(input("Digite um numero: "))
soma = 0
for i in range(1, n+1, 2):
    soma += i
print(soma)
"""

"""
Problema 7: 

Escreva um programa que leia um inteiro n e escreva a soma dos seus
divisores. Utilize um ciclo for para o efeito.

n = int(input("Digite um numero: "))
soma = 0
for i in range(0,n):
    if n % i == 0:
        soma += 0
print(soma)
"""

"""
Problema 8:

Escreva um programa que leia um inteiro n e escreva no ecrã o seu factorial.
Utilize um ciclo for para o efeito.

n = int(input("Digite um numero: "))

soma = 1
for i in range(1,n+1):
    soma *= i
print(soma)
"""
"""
Problema 9:

Escreva um programa que leia um inteiro positivo n e escreva no ecrã a soma
dos números positivos ímpares até ao número, inclusive. Para tal utilize um ciclo
for e não recorra a comandos alternativos.

n = int(input("Digite um numero: "))
soma = 0
for i in range(1, n+1, 2):
    soma += i
print(soma)
"""

"""
Problema 10:
Escreva um programa que leia dois inteiros positivos n e m e escreva no ecrã os
números entre 0 e n, enquanto a soma destes for menor que m. Use um ciclo
for para o efeito.

n = int(input("Digite um numero: "))
m = int(input("Digite um numero: "))
soma = 0
for i in range(0,n+1):
    if soma < m:
        soma += 1
"""
"""
Problema 11:


Escreva um programa que recebe um número k e escreva no ecrã uma tabela
com k linhas e k colunas, em que cada posição apresenta a multiplicação da
linha pela coluna da tabela. Para tal recorra a ciclos for. Segue um exemplo
>>> Introduza um número inteiro: 10
0 0 0 0 0 0 0 0 0 0
0 1 2 3 4 5 6 7 8 9
0 2 4 6 8 10 12 14 16 18
0 3 6 9 12 15 18 21 24 27
0 4 8 12 16 20 24 28 32 36
0 5 10 15 20 25 30 35 40 45
0 6 12 18 24 30 36 42 48 54
0 7 14 21 28 35 42 49 56 63
0 8 16 24 32 40 48 56 64 72
0 9 18 27 36 45 54 63 72 81

k = int(input("Digite um numero: "))

for n in range(0,k):
    for m in range(0, k):
        print(n*m,end=" ")
    print()
"""

"""
Problema 12:

Escreva um programa que leia um inteiro positivo n e crie um desenho igual ao
apresentado abaixo, em que largura e comprimento são iguais a n. Note que as
posições em que a linha e a coluna são pares, o símbolo apresentado é um # e
nos restantes o símbolo apresentado é um +. Para tal recorra a ciclos for.
#
+
#
+

k = int(input("Digite um numero: "))
for n in range(0, k):
    for m in range(0,k):
        if n%2 == 0 and m%2 == 0:
            print("#",end=" ")
        else:
            print("+",end=" ")
    print()

"""

"""
Problema 13:

Escreva um programa que leia um inteiro positivo n e crie um desenho igual ao
apresentado abaixo, em que largura e comprimento são iguais a n. Para tal
recorra a ciclos for.
#
+
#
+
#
k = int(input("Digite um numero: "))
for n in range(0, k):
    for m in range(0,k):
        if n > m:
            print("#",end=" ")
        else:
            print("+",end=" ")
    print()

"""
"""
Problema 14:
Escreva um programa que leia a linha de texto inserida pelo utilizador e escreva
um caracter desse texto por linha. Para tal recorra a ciclos for. Segue-se um
exemplo de interacção:
>>> Insira o texto: Hello World!
H
e
l
l
o
W
o
r
l
d
!


frase = input("digite algo: ")
for char in frase:
    print(char)
"""
"""
Problema 15:
.Escreva um programa que receba uma sequência de caracteres do utilizador e
imprima os caracteres por ordem inversa, um por linha, sem recorrer a
comandos alternativos. Recorra a ciclos for.

frase = input("digite algo: ")
for char in frase:
    print(char)
"""

"""
Problema 16:

Escreva um programa que leia um número em virgula flutuante e escreva no
ecrã a sua raiz cúbica. Recorra ao método da bissecção e garanta que a solução
calculada tenha uma precisão inferior a 0.0001. Recorra a ciclos for.

k = float(input("Digite um número com vírgula flutuante:"))

limite_inferior = 0
limite_superior = k
aproximacao = k / 2.0

valor = "a"

precisao = 0.0001
for i in range(1000):  # Limite de iterações para evitar loops infinitos
    aproximacaoCubica = aproximacao ** 3

    if abs(aproximacaoCubica - k) <= precisao:
        valor = aproximacao

    if aproximacaoCubica < k:
        limite_inferior = aproximacao
    else:
        limite_superior = aproximacao

    aproximacao = (limite_inferior + limite_superior) / 2  # Atualiza a aproximação

if valor != "a":
    print(f"A raiz cúbica de {k} é aproximadamente {valor:.4f}")
else:
    print("Não foi possível encontrar uma solução com a precisão desejada.")
"""
"""
Problema 17:

Escreva um programa que determine a raiz do polinómio x(ao quadrado) - 2x - 3 com uma
precisão inferior a 0.001. Utilize [1, 4] como intervalo inicial. Recorra a ciclos
for.

limiteInferior = 1
limiteSuperior = 4 #inclusivé
for num in range(limiteInferior,limiteSuperior+1):
    k = num**2 - 2*num -3
    limite_inferior = 0
    limite_superior = k
    aproximacao = k / 2.0

    valor = "a"

    precisao = 0.0001
    for i in range(1000):  # Limite de iterações para evitar loops infinitos
        aproximacaoCubica = aproximacao ** 3

        if abs(aproximacaoCubica - k) <= precisao:
            valor = aproximacao

        if aproximacaoCubica < k:
            limite_inferior = aproximacao
        else:
            limite_superior = aproximacao

        aproximacao = (limite_inferior + limite_superior) / 2  # Atualiza a aproximação

    if valor != "a":
        print(f"A raiz cúbica de {k} é aproximadamente {valor:.4f}")
    else:
        print("Não foi possível encontrar uma solução com a precisão desejada.")

"""