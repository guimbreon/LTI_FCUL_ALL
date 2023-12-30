def diferenca(l1, l2):
    """
    Diferença entre duas listas dadas
    requires: l1 list; l2 list
    ensures: devolve uma list que contem os elementos de l1 que não estão em 
    l2. As listas l1 e l2 não são alteradas.
    """
    result = l1
    i = 1
    while i < len(l1):
        if i in l2:
            result.remove(i)
        i += 1
    return result

