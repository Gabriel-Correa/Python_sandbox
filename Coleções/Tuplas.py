# ======================================================Características de uma tupla=================================================================
# A representação de tuplas é por (): tuple = (1, 2, 3)
# Tuplas são imutáveis. As operações com tuplas geram novas tuplas.
# Tupla precisam conter 2 ou mais itens.
# Tuplas não admitem adição ou remoção de itens, devido ao seu status de imutabilidade.

# ======================================================Gerando Tuplas=================================================================================

# Tuplas podem ser geradas com a função range:
tupla = tuple(range(11))

# ======================================================Desempacotando Tuplas==========================================================================

# Podemos desempacotar uma tupla alocando seus itens em outras variáveis:
tupla = (1, 2)
x, y = tupla

# ======================================================Funções das Tuplas=============================================================================

# Caso todos os itens sejam inteiros ou reais, é possível utilizar as funções soma, valor máximo e minimo:
sum(tuple)
max(tuple)
min(tuple)

# ======================================================Verificando o tamanho das Tuplas=============================================================================

# É possível usar o comando length também:
len(tuple)

# ======================================================Concatenando Tuplas=============================================================================

# Podemos concatenar tuplas:
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla1 + tupla2
# OBS: Não houve modificação nem na tupla1 e nem na tupla2.

# ======================================================Verificando elemntos dentro da Tupla=============================================================================

# Para verificar se determinado elemento se encontra em uma tupla:
tupla(1, 2, 3)
print(3 in tupla)

# ======================================================Iterando Tuplas=============================================================================

# Para iterar uma tupla, use a estrutura for:
for n in tupla:
    print(n)

# É possível iterar com a estrutura while:
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio')
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Para ter o indíce junto do valor, faça:
for indice, valor in tupla:
    print(indice, valor)

# ======================================================Contando itens dentro da Tupla=============================================================================

# Para contar itens dentro de uma tupla, utilize o comando .count:
tupla1.count()


# Onde usar tuplas na prática
# Utilizaremos tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção.
# EX1: meses = (janeiro, fevereiro, março ,[...], outubro, novembro, dezembro)

# Podemos verificar o indíce de um item em uma tupla: tupla.index('x')
# OBS: Caso exista duplicidade de itens, retornará o valor relativo ao primeiro item encontrado.

# Slicing: tupla[inicio : fim : passo]
