def getPhone(nome, agenda):
    """
    Número de telefone de dada pessoa.
    
    Requires: nome string representando o nome de uma pessoa,
    agenda dict representando uma agenda de telefones
    Ensures: numero telefone lst de nome na agenda 
    """
    
    return agenda.get(nome)



def getName(contato, agenda):
    """
    Nome de dado telefone dado em agenda dada.
    
    Requires: contato int representando numeros de telefone,
    agenda dict representando uma agenda de telefones
    Ensures: nome string de dado numero na agenda
    """
    out = key
    for key,value in agenda.items():
        
        if contato in value:
            out = key
    return out   
def addNum(nome, numero, agenda):
    """
    Adiciona entrada com nome e numero dados em dada agenda.
    
    Requires: nome string representando o nome de uma pessoa,
    numero int representando números de uma pessoa,
    agenda dict representado o dicionario onde estão os contatos,
    em que as chaves são strings e os valores são listas de inteiros
    Ensures: agenda é expandida com entrada com nome e numero
    """
    if nome in agenda:
        agenda[nome].append(numero)
    else:
        agenda[nome] = [numero]

def remNum(nome,agenda):
    """
    Remove contato em dada agenda.
    
    Requires: nome string representando o nome de uma pessoa,
    agenda dict representado o dicionario onde serão removidos os contatos
    Ensures: agenda é 
    """
    del agenda[nome]

