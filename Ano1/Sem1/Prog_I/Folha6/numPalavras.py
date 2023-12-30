"""
Problema 5: 
b) Uma função que conte o número de palavras de um ficheiro dado.
"""

def countWorks(ficheiro):
    """
    Conta o número de espaços em branco de um ficheiro dado.
    Requires: localização do ficheiro
    Ensures: numeros de espaços brancos
    """
    fp = open(ficheiro,"r")
    texto = fp.read()
    numBrancos = 0
    texto = texto.split(" ")
    contador = len(texto)
    for item in texto:
        if "\n" in item:
            contador += 1 
    print(texto)
    fp.close()
    return contador
