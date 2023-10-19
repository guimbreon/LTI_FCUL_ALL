"""
Problema 1
    Escreva em linguagem Python um programa que leia um número e escreva no
ecrã se este é par ou ímpar.

numero = int(input("Digite um número:\n>>>"))

if(numero % 2 == 0):
    print("par")
else:
    print("impar")
"""


"""
Problema 2
    Escreva em linguagem Python um programa que leia três números inteiros e
escreva no ecrã a soma dos que são pares e a soma dos que são ímpares.

totalNums = 3 #Alterar este número consoante a quantidade de numeros inteiros pedidos
par = 0
impar = 0


while(totalNums > 0):
    num = int(input("Digite um número:\n>>>"))
    if(num % 2 == 0):
        par += num
    else:
        impar += num
    totalNums -= 1


print("Soma par:",par)
print("Soma impar:",impar)


"""

"""
Problema 3
    Escreva em linguagem Python um programa que leia dois números inteiros e
escreva no ecrã qual é o maior. Escreva uma variante do programa que indique,
adicionalmente, quando os número são iguais. Segue-se um exemplo da interacção
com o computador (variante).
        Indique o primeiro número inteiro: 19
        Indique o segundo número inteiro: 19
        Os números são iguais.


num1 = int(input("Digite o primeiro número:\n>>>"))
num2 = int(input("Digite o segundo número:\n>>>"))

if(num1 > num2):
    print("O primeiro numero é maior que o segundo número.")
elif(num1 < num2):
    print("O primeiro numero é menor que o segundo número.")
else:
    print("Os números são iguais.")
"""

"""
Problema 4
    Como alterava o programa anterior para determinar o maior número de três
números lidos. Faça duas versões do programa: uma que não lide com a igualdade(versao 1)
e outra que tenha em conta a igualdade entre os números.(versao 2)


# versão 1
num1 = int(input("Digite o primeiro número:\n>>>"))
num2 = int(input("Digite o segundo número:\n>>>"))
num3 = int(input("Digite o terceiro número:\n>>>"))

if(num1 > num2):
    if(num1 > num3):
        print("O primeiro numero é o maior.")
    else:
        print("o terceiro número é o maior")
else:
    if(num2 > num3):
        print("O segundo numero é o maior.")
    else:
        print("o terceiro número é o maior")    



# versão 2
num1 = int(input("Digite o primeiro número:\n>>>"))
num2 = int(input("Digite o segundo número:\n>>>"))
num3 = int(input("Digite o terceiro número:\n>>>"))

if(num1 == num2 == num3):
    print("Os números são iguais.")
else:
    if(num1 > num2):
        if(num1 > num3):
            print("O primeiro numero é o maior.")
        else:
            print("o terceiro número é o maior")
    else:
        if(num2 > num3):
            print("O segundo numero é o maior.")
        else:
            print("o terceiro número é o maior")    

"""


"""
Problema 5
    Escreva em linguagem Python um programa que leia um número inteiro positivo
(menor ou igual a 5) e escreva no ecrã a sua representação em numeração
romana. Segue-se um exemplo da interacção com o computador (em itálico os
dados introduzidos pelo utilizador).
        Diga um número: 4
        IV


numero = int(input("Digite um numero:\n>>>"))
if(numero == 1):
    print("I")
elif(numero == 2):
    print("II")
elif(numero == 3):
    print("III")
elif(numero == 4):
    print("IV")
elif(numero == 5):
    print("V")
else:
    print("Out of range.\nShould be (1-5)!")
"""

"""
Problema 6
    Escreva em linguagem Python um programa que leia o ano, o mês e o dia de
nascimento de uma pessoa e escreva no ecrã a idade no dia de hoje. Refine o
programa de forma a escrever a palavra ano ou anos consoante a idade da pessoa.

diaHoje = int(input("Que dia é hoje?\n>>>"))
mesHoje = int(input("Em que mês estamos?\n>>>"))
anoHoje = int(input("Em que ano estamos?\n>>>"))


diaAniv = int(input("Em que dia nasceu?\n>>>"))
mesAniv = int(input("Em que mês nasceu?\n>>>"))
anoAniv = int(input("Em que ano nasceu?\n>>>"))

if(diaHoje >= diaAniv and (mesHoje >= mesAniv)):
    print(anoHoje-anoAniv)
else:
    print(anoHoje-anoAniv-1)
"""

"""
Problema 7
    Escreva em linguagem Python um programa que leia quatro números inteiros
(um de cada vez) e escreva após cada interação qual o menor número lido até ao
momento. Segue-se um exemplo da interacção com o computador.
        Introduza um número inteiro: 4
        O menor número introduzido até agora é 4.
        Introduza um número inteiro: 6
        O menor número introduzido até agora é 4.
        Introduza um número inteiro: 2
        O menor número introduzido até agora é 2.

totalNumeros = 3
menor = 100000000 #mudar?
while(totalNumeros > 0):
    numero = int(input("Introduza um número inteiro"))
    if menor > numero:
        menor = numero
    print("O menor número introduzido até agora é",menor)
    totalNumeros -= 1
"""

"""
Problema 8
    Escreva em linguagem Python um programa que leia um ano (> 0) e escreva no
ecrã o século a que este ano pertence. Relembre que o ano 1999 faz parte do
século XX, 2000 ainda faz parte do século XX e que 2001 é o primeiro ano do
século XXI. Desenvolva uma versão do programa utilizando um comando
alternativo e outra utilizando apenas uma expressão numérica. Note que
int(True)=1 e que int(False)=0.

ano = int(input("Insira um ano:\n>>>"))
if ano > 99:
    if(ano > 0):
        if(str(ano)[-2:] == "00"):           
            seculo = int(str(ano)[0:-2])
        else:
            seculo = int(str(ano)[0:-2]) +1
        print("Seculo",seculo)

    else:
        print("O ano tem que ser maior que 0!")
else:
    print("Seculo 1")
"""

"""
Problema 9
    Escreva em linguagem Python um programa que leia o ano (> 1900) e mês (1-
12) e escreva no ecrã o número de dias do mês. Note que um ano (não secular) é
bissexto se for divisível por 4. Os anos seculares são bissextos se forem divisíveis
por 400.

ano = int(input("Digite um ano: \n>>>"))

mes = int(input("Digite um mes: \n>>>"))

if(ano > 1900) and (1 <= mes <= 12):
    if(ano % 4 == 0) or (str(ano)[-2:] == "00"):
        if(mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            print("31")
        elif(mes == 2):
            print("29")
        elif(mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            print("30")
    else:
        if(mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            print("31")
        elif(mes == 2):
            print("28")
        elif(mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            print("30")

"""

"""
Problema 10
    Escreva um programa em Python que leia dois números inteiros e escreva no
écran o quadrado do maior a multiplicar pelo quadrado do primeiro. Se os números
forem iguais o programa deve escrever apenas “iguais”, e se forem ambos zero
deve escrever também “e ambos zero!”

num1 = int(input("Digite o primeiro numero:\n>>>"))

num2 = int(input("Digite o segundo numero:\n>>>"))

if(num1 == num2 == 0):
    print("iguais a zero")
elif(num1 == num2):
    print("iguais")
else:        
    if(num1 > num2):
        print(num1**2*num2**2)
    elif(num1 < num2):
        print(num2**2*num1**2)

"""

"""
Problema 11
Escreva em linguagem Python um programa que leia uma data (ano, mês e dia
em separado) e um número inteiro x, e devolva uma nova data x dias mais à
frente.

"""
continuar = True
dia = int(input("Que dia quer trabalhar?\n>>>"))
mes = int(input("Que mês quer trabalhar?\n>>>"))
ano = int(input("Que ano quer trabalhar?\n>>>"))
aMais = int(input("Quantos dias para a frente:\n>>>"))+1

while aMais > 0 and continuar:
    if ano > 1900 and 1 <= mes <= 12:
        dias_no_mes = 31

        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            dias_no_mes = 30
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                dias_no_mes = 29
            else:
                dias_no_mes = 28

        dias_faltando = dias_no_mes - dia + 1

        if aMais >= dias_faltando:
            aMais -= dias_faltando
            dia = 1
            mes += 1

            if mes > 12:
                mes = 1
                ano += 1
        else:
            dia += aMais
            aMais = 0

        print(f"{dia:02d}/{mes:02d}/{ano}")
    else:
        print("Data inválida.")
        continuar = False

if continuar:
    print(f"Final: {dia:02d}/{mes:02d}/{ano}")
