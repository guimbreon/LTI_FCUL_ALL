"""
Problema 1:

Considere o seguinte programa:
number = 7 
guess = -1 
print("Adivinha o número!")
while guess != number: 
 guess = int(input("Será... ")) 
 if guess == number: 
 print("Viva! Adivinhaste!")
 elif guess < number: 
 print("É maior...")
 elif guess > number: 
 print("Não é tão grande.")
Modifique-o de modo a que o número a adivinhar seja gerado aleatoriamente. 
Recorra a um módulo das bibliotecas Python.

"""
import random

limInf = int(input("Qual o limite inferior: "))
limSup = int(input("Qual o limite superior: "))

number = random.randint(limInf,limSup)
guess = -1 
print("Adivinha o número!")
while guess != number: 
    guess = int(input("Será... ")) 
    if guess == number: 
        print("Viva! Adivinhaste!")
    elif guess < number: 
        print("É maior...")
    elif guess > number: 
        print("Não é tão grande.")
