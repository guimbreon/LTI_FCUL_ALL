"""
Problema 5 - Construa um módulo para manipulação de ficheiros de texto que contenha as 
seguintes funções:
a) Uma função que conte o número de espaços em branco de um ficheiro dado.

"""
def countBlank(ficheiro):
    """
    Conta o número de espaços em branco de um ficheiro dado.
    Requires: localização do ficheiro
    Ensures: numeros de espaços brancos
    """
    fp = open(ficheiro,"r")
    texto = fp.read()
    numBrancos = 0
    for c in texto:
        if c == " ":
            numBrancos += 1
    return numBrancos
    



