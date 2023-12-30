"""
2) Construa o seguinte:

c) Um programa que recorrendo aos módulos desenvolvidos nas alíneas
anteriores, peça ao utilizador um valor e escreva no ecrã o perímetro e a área
do círculo e do quadrado em que o valor dado corresponde à medida do raio e
do lado.
"""
import Folha6_2a, Folha6_2b
ladoQuadrado = int(input("Lado quadrado é:"))

raioCirculo = int(input("Raio do circulo é:"))

print(Folha6_2a.area(raioCirculo),Folha6_2a.perimetro(raioCirculo))


print(Folha6_2b.quadradoPerimetro(ladoQuadrado),Folha6_2b.quadradoArea(ladoQuadrado))