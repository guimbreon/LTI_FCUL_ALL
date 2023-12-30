"""
1) Considere a frase "Há limites para aquilo que o POVO português pode
aguentar." e crie uma variável famous_quote com esta frase. Usando métodos da
classe String, construa um programa que
a) Imprima o número de vezes que a sequência "po" ocorre em famous_quote.
b) Imprima o resultado de passar todos os caracteres de famous_quote a
minúsculas.
c) Imprima o resultado de substituir todas as ocorrências em famous_quote de "a"
por "o" e todas as ocorrências de "o" por "a".
d) Imprima a lista de subsequências que resultam de quebrar famous_quote nos
espaços em branco.
e) Depois de remover espaços em branco repetidos, imprima a lista de
subsequências que resultam de quebrar famous_quote nos caracteres "u" e "t".
f) Imprima o resultado de substituir em famous_quote os caracteres nas posições
pares por "2".
"""
famous_quote = "Há limites para aquilo que o POVO português pode aguentar."

#a)
print("Número total de 'po' na frase:",famous_quote.count("po"))
#b)
print(famous_quote.lower())
#c)
print(famous_quote.replace("a","o"))
#d)
print(famous_quote.split(" "))
#e)
spliters = ["u","t"]
quote = famous_quote.replace(" ","")
resultado = []
for spliter in spliters:
    for item in quote.split(spliter):    
        resultado.append(item)

print(resultado)
#f)
resultado_2 = ""
quote = famous_quote
for i in range(len(quote)):
    if i % 2 == 0:
        resultado_2 += "2"
    else:
        resultado_2 += quote[i]
print(resultado_2)