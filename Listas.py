# ======================================================Características de uma lista=====================================================================================

# Listas não tem tamanho definido, assim como não há tipagem específica, aceitando qualquer tipo;
# Representação de listas: [];

# ======================================================Organizar em forma Crescente==========================================================================

# Para ordenar uma lista basta usar o comando .sort(): 'lista.sort';
lista = [3, 2, 1]
lista.sort()
# O retorno será [1, 2, 3]

# ======================================================Organizando em forma Decrescente================================================================================================

# Para inverter a ordem dos itens de uma lista, basta utilizar o comando .reverse: lista.reverse()
lista = [1, 2, 3]
lista.reverse()
# O retorno será [3, 2, 1]

# ======================================================Verificando Valores================================================================================================

# Para verificar se determinado valor se encontra dentro de uma lista, basta usar o comando if: if 'x' in lista;
lista = ['x']
if 'x' in lista:
    print("Verdadeiro")

# Para verificar quantas vezes determinado valor aparece em uma lista, utilize: lista.count('x')
lista = [1, 1, 1, 2, 3]
lista.count(1)
# O retorno será 3

# ======================================================Adicionando itens na lista================================================================================================

# Caso queira adicionar itens a uma lista, utilizar o comando .append: lista.append('x');
# OBS: Com o comando .append, só conseguimos adicionar um item por vez. Se forem adicionados mais de um item por vez, será adicionado em forma de sublista.
# Ex: Lista1 = [1, 2, 3]>>> lista1.append(4, 5, 6)>>> lista1 = [1, 2, 3, [4, 5, 6]];
lista = ['Gabriel']
lista.append("Correa")
# Neste primeiro caso, o retorno será ['Gabriel', 'Correa']
lista.append("Correa", "da", "Silva")
# Aqui, o retorno será ['Gabriel', ['Correa', 'da', 'Silva']]

# Para adicionar 2 ou mais itens em uma lista, sem que ocorra uma sublista, usar o comando .extend: lista.extend([x, y, z]) ou lista.extend('Gabriel');
lista = ['Gabriel']
lista.extend("Correa", 'da', 'Silva')
# Diferente do Append, aqui não será criada uma sublista, retornando apenas ['Gabriel', 'Correa', 'da', 'Silva']

# OBS: Utilizando o .append ou .extend, o item irá para o final da lista.

# É possível adicionar itens em lugares específicos de uma lista com o comando .insert: lista.insert('local que o item ocupará, 'x')
lista = [4, 5, 6]
lista.insert(2, 3)
# O retorno vai ser [4, 5, 2, 6]

# ======================================================Juntando Listas================================================================================================

# Junte listas utilizando o símbolo de soma: lista + lista2
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
# O retorno vai ser [1, 2, 3, 4, 5, 6]

# Ou utilizando o comando .extend: lista1.extend(lista2) (nesta não será criada uma nova lista, sendo a lista2 inserida na lista1)
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
# O retorno aqui é lista1 = [1, 2, 3, 4, 5, 6] e a lista2 = [4, 5, 6]

# ======================================================Copiando uma lista================================================================================================

# Copiando uma lista para outra(Shallow copy e Deep copy)
# Forma 1(Deep Copy) cria uma nova lista, independente da original: Utilizando o comando .copy
lista1 = [6, 7, 8]
lista_copiada = lista1.copy()
# Neste caso, a lista1 e lista_copiada são independentes entre si, podendo modificar uma, sem alterar a outra

# Forma 2(Shallow copy) gera uma segunda lista, igual e dependente entre si: lista_nova = lista_original
lista1 = [6, 7, 8]
lista_copiada = lista1
# Aqui, caso eu modifique uma das listas, a outra sofrerá a mesma modificação

# ======================================================Verificando o tamanho de uma Lista=======================================================================================

# Para saber o tamanho de uma lista, utilize o comando len(abreviação de length): (len(lista))
lista = [0, 9, 8]
len(lista)
# O retorno será 3

# ======================================================Removendo itens de uma lista=======================================================================================

# Para remover o ultimo item de uma lista, utilize o comando .pop: lista.pop()
# OBS: O retorno deste comando é o item removido.
lista = [1, 2, 3]
lista.pop()
# O retorno do pop será 3, posto que é o último item da lista

# É possível tb remover um elemento com base no seu indíce
lista = [1, 2, 3]
lista.pop(2)
# O retorno do pop será 3, posto que este ocupa o indice 2 na lista
lista = [1, 2]

# Para limpar uma lista, basta utilizar o comando .clear: lista.clear()

# ======================================================Repetindo elementos=======================================================================================

# Caso queira repetir os elementos de uma lista, utilize o símbolo de multiplicação (*): lista*x
lista = [1, 2, 3]
lista * 3
# O retorno será [1, 2, 3, 1, 2, 3, 1, 2, 3]

# ======================================================Transformando string em Lista=======================================================================================

# Para transformar uma string em lista, use o comando .split(): a = "Gabriel Correa">> a = a.split()>> a = ["Gabriel", "Correa"];
# OBS: Por padrão, .split separa os elementos pelo espaço entre eles
# OBS2: Podemos informar qual o critério para separar os elementos: lista.split(",")

# O caminho inverso, de lista para string, é possível utilizando o comando .join: ' '.join(lista), neste caso, será alocado um espaço entre cada item e será convertido em string

# ======================================================Iterando Lista=======================================================================================

# Para iterar uma lista, utilize a estrutura for: lista[1, 2, 3]>> for n in lista: print(n)>>1 2 3

# ======================================================Encontrando indice de um item na Lista=======================================================================================

# Para identificar em que posição um item se encontra dentro de uma lista, utilize a estrutura for: for indice, x in enumrate(lista)
# Pode-se utilizar também o comando .index: lista.index(x), o retorno desta linha sera o indíce do item.
# OBS: Caso haja duplicidade entre os itens, o retorno será referente ao primeiro encontrado: lista = [5, 4, 5]>lista.index(5)>> 0
# OBS2: É possível utilizar ranges para buscar indíces: lista.index(o valor a ser indexado, inicio do range, fim do range)

# ======================================================Slice=======================================================================================

# Slice: lista[inicio:fim:passo]

# ======================================================Invertendo uma lista=======================================================================================

# Para inverter uma lista, utilize o comando .reverse: lista.reverse()

# ======================================================Funções matemáticas com listas=======================================================================================

# Lista com apenas numeros int:
# funções com lista, sum(lista, somará a lista); max(lista, retornará o maior valor da lista); min(lista, retornará o menor valor)

# ======================================================Convertendo Lista em Tupla=======================================================================================

# Para converter uma lista em tupla, basta usar o comando tuple(): tuple(lista)

# ======================================================Desempacotando Listas=======================================================================================

# Desempacotar lista: lista[1, 2, 3]>> num1, num2, num3 = lista>> num1 = 1; num2 = 2; num3 = 3
# OBS: A quantidade de itens precisa ser igual a quantidade de variáveis que irão receber.

# =============================================================================================================================================
