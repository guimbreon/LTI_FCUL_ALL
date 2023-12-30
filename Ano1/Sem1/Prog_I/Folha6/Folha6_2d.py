"""
Problema 2-
c) Um programa que recorrendo aos módulos desenvolvidos nas alíneas 
anteriores, peça ao utilizador um valor e escreva no ecrã o perímetro e a área 
do círculo e do quadrado em que o valor dado corresponde à medida do raio e 
do lado.

"""
import  Folha6_2a
valor = int(input("Qual o comprimento do raio: "))

print(Folha6_2a.perimetro(valor))

print(Folha6_2a.area(valor))
