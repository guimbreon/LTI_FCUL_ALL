"""
2) Construa o seguinte:

a) Um módulo que disponibiliza operações com círculos, nomeadamente, cálculo 
do perímetro e da área dado o comprimento do raio.
"""
import math
def perimetro(raio):
    return 2 * math.pi * raio
def area(raio):
    return math.pi * (raio**2)
