"""
Problema 1
    Escreva um programa em linguagem Python que leia dois números inteiros e
escreva no écran a sua soma, o seu produto, a subtração do primeiro pelo segundo,
a divisão do primeiro pelo segundo, o resto da divisão do primeiro pelo segundo, e
a potência do primeiro elevado ao segundo.

firstNumber = int(input("Digite o primeiro numero:\n>>"))
secondNumber = int(input("Digite o segundo numero:\n>>"))

print("A soma entre os numeros inseridos é:",firstNumber+secondNumber)

print("O produto entre os numeros inseridos é:",firstNumber*secondNumber)

print("A subtração entre os numeros inseridos é:",firstNumber-secondNumber)

print("A divisão entre os numeros inseridos é:",round(firstNumber/secondNumber,2))

print("O resto da divisao entre os numeros inseridos é:",firstNumber%secondNumber)

print("A potência dos numeros inseridos é:",firstNumber**secondNumber)
"""

"""
Problema 2
    Escreva em linguagem Python um programa que leia dois números em vírgula
flutuante e imprima a sua soma, a sua diferença, o seu produto e o primeiro
elevado ao segundo.

firstNumber = float(input("Digite o primeiro numero:\n>>"))
secondNumber = float(input("Digite o segundo numero:\n>>"))

print("A soma entre os numeros inseridos é:",round(firstNumber+secondNumber,2))

print("O produto entre os numeros inseridos é:",round(firstNumber*secondNumber,2))

print("A subtração entre os numeros inseridos é:",round(firstNumber-secondNumber,2))

print("A divisão entre os numeros inseridos é:",round(firstNumber/secondNumber,2))

print("O resto da divisao entre os numeros inseridos é:",round(firstNumber%secondNumber,2))

print("A potência dos numeros inseridos é:",round(firstNumber**secondNumber,2))
"""

"""
Problema 3
    Escreva em linguagem Python um programa que leia três números inteiros
correspondentes ao comprimento, largura e altura de um paralelepípedo e escreva
no écran o seu volume.

comprimento = int(input("Que comprimento deseja usar?\n>>"))

largura = int(input("Que largura deseja usar?\n>>"))

altura = int(input("Que altura deseja usar?\n>>"))

volumeParale = comprimento * largura * altura

print("O volume do paralelepípedo é",volumeParale)
"""

"""
Problema 4
    Escreva em linguagem Python um programa que leia três números inteiros e
escreva no écran a sua média. Altere o programa de forma ao valor ser o inteiro
que se obtém por truncar a parte decimal do resultado.

numero1 = int(input("Digite o primeiro numero:\n>>"))
numero2 = int(input("Digite o segundo numero:\n>>"))
numero3 = int(input("Digite o terceiro numero:\n>>"))

media = int((numero1+numero2+numero3)/3)

print("A media é:",media)
"""

"""
Problema 5
    Escreva em linguagem Python um programa que leia uma temperatura em graus
Fahrenheit e escreva a correspondente em graus Celsius.
A fórmula utilizada para a conversão de graus Fahrenheit em graus Celsius é:
                        C = (F - 32) / 1.8


Fahrenheit = int(input("Qual a temperatura em graus Fahrenheit?\n>>"))

Celsius = int((Fahrenheit - 32)/1.8)

print("Em celcius é:",Celsius)

"""

"""
Problema 6
    Escreva em linguagem Python um programa que leia o ano de nascimento de
uma pessoa e escreva no écran a idade que terá no final do ano actual. Segue-se
um exemplo da interação com o computador.
Indique o ano de nascimento: 1972
No final de 2015 terá 42 ano(s).

idade = int(input("Indique o ano de nascimento:\n>>"))

idade = 2023 - idade

print("No final de 2023 terá" , idade , "Ano(s)")
"""
"""
Problema 7
    Escreva em linguagem Python um programa que determine o valor em cêntimos
de todas as moedas castanhas num mealheiro. Leia do teclado valores inteiros
representando o número de moedas de 5, 2, e 1 cêntimos.

moeda1 = int(input("Digite o numero de moedas de 1 centimo que tens:\n>>"))
moeda2 = int(input("Digite o numero de moedas de 2 centimo que tens:\n>>"))*2
moeda5 = int(input("Digite o numero de moedas de 5 centimo que tens:\n>>"))*5

dinheiro = moeda1 + moeda2 + moeda5

print("Tens",dinheiro,"centimos")
"""
"""
Problema 8
    Escreva em linguagem Python um programa que descreva um número inteiro
entre 0 e 999, em termos do número de centenas, número de dezenas e número
de unidades. Por exemplo, para 304 o resultado pretendido é “3 centenas 0
dezenas e 4 unidades”.

numero = input("Digite o número que quer trabalhar:\n>>")
lista = list(numero)
if not numero.isdigit() or int(numero) < 0 or int(numero) > 999:
    quit("Você deve inserir apenas números de 0 a 999. Tente novamente.")

if(len(lista) == 3):
    print(lista[0] , "centenas ",lista[1],"dezenas",lista[2],"unidades")
elif(len(lista) == 2):
    print(lista[0],"dezenas",lista[1],"unidades")
else:
    print(lista[0],"unidades")
    """
"""
Problema 9
    Escreva em linguagem Python um programa que leia um intervalo de tempo em
horas, minutos e segundos, e que depois imprima o número de segundos
equivalente. Por exemplo, 1 hora, 28 minutos e 42 segundos é equivalente a 5322
segundos.


horas = int(input("Quantas horas deseja usar?\n>>"))

minutos = int(input("Quantos minutos deseja usar?\n>>"))

segundos = int(input("Quantos segundos deseja usar?\n>>"))

totalSegundos = horas*3600 + minutos*60 + segundos
print("Isso é equivalente a:",totalSegundos,"segundos.")
"""
"""
Problema 10
    Desenvolva a versão inversa do problema anterior: lê um número
representando uma duração em segundos e imprime o seu equivalente em horas,
minutos e segundos. Por exemplo, 9999 segundos é equivalente a 2 horas, 46
minutos e 39 segundos


segundos = int(input("Quantos segundos deseja usar?\n>>"))

horas = segundos/3600

minutos = (horas - int(horas))*60

restoSegundos = (minutos - int(minutos))*60

print(int(horas),"horas",int(minutos),"minutos",round(restoSegundos),"segundos")
"""