"""
Arrays podem ser unidimensionais: Arrays/vetores
ou Multidimensionais: matrizes

Em python, esta estrutura é conhecida como lista
"""

numeros = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ] # Matriz 3x3

# Para buscar um dado nesta lista utiliza-se os indíces:

print(numeros[0][1]) # Primeiro indice se refere a linha, já o segundo, sobre a coluna

# Iterando uma lista aninhada:

for lista in numeros:
    print(lista)
    for numero in lista:
        print(numero)

[[print(valor) for valor in lista] for lista in numeros] # Iterando com Comprehension

