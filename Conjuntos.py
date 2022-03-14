# Conjuntos, em qualquer linguagem de programação, fazemos referência à Teoria dos conjuntos da matemática
# Em python, os conjuntos chamam-se Sets
# Sets(conjuntos) não possuem valores duplicado
# Sets(conjuntos) não possuem valores ordenados
# Itens não são acessados via índice, ou seja, Sets não são indexados

# Sets são úteis quando precisamos armazenar itens, mas sua ordenação é indiferente, assim como não precisarmos nos preocupar com chaves:valores e itens duplicados

# Sets são representados com {}

# Diferença entre Sets e mapas(dicionarios):
# Um dicionário possue chave:valor, Sets apenas possuem valores

# Definindo um Set:

# Forma 1:
# Mesmo com duplicidade de dados, quando criado, o conjunto retirará os itens duplicados
conjunto = set({1, 2, 3, 4, 6, 5, 7, 2, 3})

# Forma 2:
# Igualmente aqui, os dados duplicados serão excluídos quando dá criação do Set
conjunto = {1, 2, 3, 6, 5, 4, 3, 2, 1}


# É possível verificar se x item existe em um conjunto:
if 3 in conjunto:
    print("Há o item")
else:
    print("Não há o item")

# Importante lembrar que além de não haver duplicidade de valores, não há ordem entre os itens.

# É possível usar todos os tipos de dados misturados em um set.
Conjunto_exemplo = {1, 'b', True, 1.5}

# Podemos iterar um Set usando o padrão for:
for item in conjunto:
    print(item)

# Adcionando itens em um Set:
conjunto.add("valor")

# Removendo itens de um Set:

# Forma 1:

# Aqui removemos o item do conjunto, não se refere ao indíce. Nâo há retorno deste comando, sendo o item descartado.
conjunto.set(3)

# OBS: Caso não haja correspondência, será gerado KeyError

# Forma 2:

conjunto.discard(2)

# OBS: Caso não haja correspondência, o código seguirá, ignorando este comando.

# Copiando um Set para outro Set:

# Forma 1 (Deep Copy):
# É criada um segundo Set, independente do Set original.
novo_set = conjunto.copy()

# Forma 2 (Shallow Copy):
novo_set2 = conjunto  # Ambos os sets ficam vinculados.

# Podemos remover todos os itens no Set:
conjunto.clear()

# Métodos matemáticos dos Sets:

# Juntando Sets:
alunos_python = {"Gabriel", "Rafael"}
alunos_java = {"Cristiane", "Ricardo", "Gabriel"}
alunos = alunos_java.union(alunos_python)  # Forma 1 (RECOMENDADA)

alunos_forma2 = alunos_python | alunos_java  # Forma 2

# Filtrando itens em comum entre os Sets:
alunos_em_comum = alunos_python.intersection(alunos_java)  # Forma 1

alunos_em_comum2 = alunos_python & alunos_java  # Forma 2

# Filtrando itens que são exclusivos entre os Sets:
only_python = alunos_python.difference(alunos_java)

only_java = alunos_java.difference(alunos_python)

# Soma(sum(conjunto)), Valor máximo(max(conjunto)), Valor mínimo(min(conjunto)) e tamanho(len(conjunto)):
# OBS: Todos os valores precisam ser ou int, ou float.
