import copy
def diferenca(l1, l2):
    """
    Diferença entre duas listas dadas
    requires: l1 list; l2 list
    ensures: devolve uma list que contem os elementos de l1 que não estão em 
    l2. As listas l1 e l2 não são alteradas.
    >>> diferenca([ ],[ ])
    []
    >>> diferenca([13],[ ])
    [13]
    >>> diferenca([ ],[13])
    []
    >>> diferenca([1,1,1],[2,2,2])
    [1, 1, 1]
    >>> diferenca([1,1,1],[1,31,1])
    []
    >>> diferenca([1,31,1],[1,1,1])
    [31]
    """
    result = copy.deepcopy(l1)
    i = 0
    while i < len(l1):
        if l1[i] in l2:
            result.remove(l1[i])
        i += 1
    return result

#a
##if __name__ == "__main__":
##    import doctest
##    doctest.testmod()
diferenca([6,1,5,1,6,2,7], [1,2,3])
