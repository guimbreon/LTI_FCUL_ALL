"""
4) Construa uma função que receba um ficheiro de texto como parâmetro e
devolva um dicionário com cada uma das palavras do texto associada à lista de
linhas em que ocorre no texto. Implemente instruções que testem a função.
"""

def dictFromText(Text):
    """
    Dicionário de dado texto

    Requires: Text str representando endereço de ficheiro de texto
    Ensures
    """

    fp = open(Text)
    dictText = {}
    lineNum = 0
    for line in fp:
        lineNum += 1
        for word in line.split(" "):
            if word in dictText:
                dictText[word].append(lineNum)
            else:
                dictText[word] = [lineNum]
    fp.close()
    return dictText
    
dictText = dictFromText("U:/PI/Folha 8/dados.txt")
for key, values in dictText.items():
    print(key, values)
