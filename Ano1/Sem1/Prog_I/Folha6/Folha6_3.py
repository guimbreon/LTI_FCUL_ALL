import math
"""
3) Construa um módulo que contenha operações definidas sobre polígonos regulares
genéricos. As operações devem calcular o perímetro e a área de um polígono
regular dados o número de lados e o comprimento de um lado. Lembre-se que o
perímetro é a soma dos comprimentos de todos os lados e a área é o produto do
apótema pelo perímetro sobre 2.

raio = 1/2 * lado * sin^(-1)(pi/n)

apotema = 1/2 * lado * cot(pi/n)
"""

def perimetroPoligono(lado,n):
    """
    Usado para calcular o perimetro do poligono.

    Requires:
    - lado (int): comprimento de lados de um dado poligono
    - n (int) : numero de lados  de um dado poligono
    Ensures:
    - perimetro (int) : perimetro de um dado poligono
    """
    return lado * n

def areaPoligono(lado,n):
    """
    Usado para calcular o perimetro do poligono.

    Requires:
    - lado (int): comprimento de lados de um dado poligono
    - n (int) : numero de lados  de um dado poligono
    Ensures:
    - area (int) : area de um dado poligono
    """
    area = (n * lado**2) / (4 * math.tan(math.pi / n))
    return area

def encontrarPoligono(tolerancia):
    raio = 1.0
    n = 3  # Começamos com um triângulo

    while True:
        comprimentoAnterior = 2 * raio * math.sin(math.pi / n)
        n += 1
        comprimentoAtual = 2 * raio * math.sin(math.pi / n)

        diferenca = abs(comprimentoAtual - comprimentoAnterior)

        if diferenca < tolerancia:
            break

    return n
print(areaPoligono(10,10))

#a
tolerancia = 0.001

numeroLados = encontrarPoligono(tolerancia)
print(numeroLados)