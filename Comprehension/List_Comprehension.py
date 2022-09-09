"""
List Comprehension

Meio pelo qual é possível gerar novas listas com dados processados, a partir de outro dado iterável

Sintaxe: [dado for dado in iterável]
"""

numeros = [1, 2, 3, 4, 5]
exemplo_list_comprehension = [numero*10 for numero in numeros]
print(exemplo_list_comprehension)

# É possível utilizar funções dentro da list comprehension:

numeros_Quadrado = [1, 2, 3, 4, 5]

def quadrado(valor):
    resultado = valor * valor
    return resultado

list_comprehension_funcao = [quadrado(numero) for numero in numeros_Quadrado]
print(list_comprehension_funcao)

# Diferença de comprehension e loops:

# Loop:

numeros_loop = [1, 2, 3, 4, 5]

numeros_dobrados_loop = []

for n in numeros_loop:
    numeros_dobrados = n*2
    numeros_dobrados_loop.append(numeros_dobrados)

print (numeros_dobrados_loop)

# Comprehension:

print([n*2 for n in numeros_loop])


# É possível adicionar estruturas lógicas a este sistema:

numeros_lógica = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros_lógica if numero%2 == 0]
impares = [numero for numero in numeros_lógica if numero%2 != 0]

print(pares)
print(impares)

