# ======================================================Características de um Dicionário======================================================================================

# Em algumas linguagens, dicionários são conhecidos como mapas.
# Dicionários são coleções chave:valor
# A representação é via {}
# Separa-se chave do valor pelos :
# Chave e valor podem ser de qualquer tipo de dado
# Podemos misturar tipos de dados
# Dicionários não aceitam duplicidade de chaves
# Podemos utilizar qualquer tipo nos dicionários (int, float, str, boolean), assim como tuplas, listas e afins como chaves
locais = {
    ('rua joao', 'bairro protasio'): 'Casa',
    ('rua manoel', 'bairro rubem berta'): 'faculdade'
}

# ======================================================Criando Dicionários=======================================================================================

# Criação de Dicionários:
# Forma 1:
paises = {'br': 'Brasil'}
# Forma 2:
paises = dict(br='Brasil')

# ======================================================Acessando itens======================================================================================

# Acessando elementos de um dicionário
# Forma 1: Acessando via chave
paises['br']
# OBS: Caso utilize uma chave inexistente, retornará erro KeyError

# Forma 2: Acessando via get (recomendada)
paises.get('br')
# OBS: Caso utilize uma chave inexistente, retornará None

# Criando dicionário de forma não usual:
dicionario = {}.fromkeys('chave', 'valor')
# ======================================================Verificando a existência de itesn=======================================================================================

# É possível verificar a existência de uma chave em um dicionário:
print('br' in paises)
# OBS: Não podemos buscar valor neste caso, apenas chaves.

# ======================================================Adicionando/Atualizando elementos em um dicionário=======================================================================================

# Adicionando elemenos no dicionário:
# Forma 1:
dicionario = {'chave': 'valor'}
dicionario['chave'] = 'valor'
# Forma 2:
dado_novo = {'chave': 'valor'}
dicionario.update(dado_novo)

# Atualizando dados no dicionário:
# Forma 1:
# adicionar e atualizar valores compartilham o mesmo metodos
dicionario['chave'] = 'valor novo'

# ======================================================Removendo itens de um dicionário=======================================================================================

# Removendo dados de um dicionário:
# Forma 1:
dicionario.pop('chave')  # utilizar a chave para realizar a remoção do item.

# Forma 2:
del dicionario['chave']  # Este metódo não retorna valor algum

# ======================================================Limpando um dicionário=======================================================================================

# limpar dicionário, use .clear()

# ======================================================Copiando Dicionários=======================================================================================

# copiando um dicionario para outro:
# Forma 1 (Deep Copy):
copia_dicionario = dicionario.copy()

# Forma 2 (Shallow Copy):
copia_dicionario = dicionario

# Criando dicionário de forma não usual:
dicionario = {}.fromkeys('chave', 'valor')

# ======================================================Iterando um dicionário=======================================================================================

# Como iterar um dicionário:

# Aqui imprimimos as chaves:
for chave in dicionario:
    print(chave)

# Aqui imprimimos os valores:
for chave in dicionario:
    print(dicionario[chave])

# Aqui imprimimos tanto a chave quanto o valor:
for chave in dicionario:
    print(f'{chave} : {dicionario[chave]}')

# ======================================================Desempacotando um dicionário=======================================================================================

# Desempacotando dicionarios:
print(dicionario.items())

# ======================================================Acessando dados em um dicionário=======================================================================================

# Como acessar todas as chaves:
print(dicionario.keys())

# Como acessar todos os valores:
print(dicionario.values())

# ======================================================Métodos de um dicionário=======================================================================================

# Usando as funções soma(sum()), valor máximo(max()), valor mínimo(min()) e tamanho(len()):
# OBS: Todos os valores precisam ser inteiros ou floats.
print(sum(dicionario.values()))

print(max(dicionario.values()))

print(min(dicionario.valeus()))

print(len(dicionario))
