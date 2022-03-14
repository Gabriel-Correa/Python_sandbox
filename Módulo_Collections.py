# Módulo Counter:

# Recebe um iterável como parâmetro e cria um objeto do tipo Collections-Counter que é parecido com um Dicionário
# Possuindo chave e valor, sendo a chave o valor passado como parametro e o valor referente a quantidade ocorrências da chave.
from collections import deque
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import Counter

exemplo = [1, 2, 3, 4, 5, 6, 6, 7, 7, 7, 8, 8, 8]
exemplo_counter = Counter(exemplo)
# Retorno: Counter({7: 3, 8: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
print(exemplo_counter)

# Encontrando os itens com maior ocorrência no objeto iterável:
exemplo_counter.most_common(1)


# Módulo Default Dict:

# Criando um dicionário com a função Default Dict, informamos um valor Default. É possível usar um lambda para isso, tal valor será chamado quando não
# houver um valor definido, evitando quebrar o código com KeyError e caso tentarmos acessar uma chave inexistente, essa chave será criada com o valor Default.

# OBS: Lambdas são funções sem nomes que podem ou não receber valores de entrada e retornar valores


dicionario = defaultdict(lambda: 0)
dicionario['nome'] = 'Gabriel'


# Módulo Ordered Dict:

# Ordered Dict garante a ordem de inserção dentro do dicionário

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3})


# Módulo Named Tuple:

# São tuplas que especificamos um nome e parâmetros.

# Necessário definir um nome e parâmetros:
# Declarando a Named Tuple
# Forma 1:
exemplo = namedtuple('nome', 'primeiro_nome segundo_nome')

# Forma 2:
exemplo2 = namedtuple('nome', 'primeiro_nome, segundo_nome')

# Forma 3:
exemplo3 = namedtuple('nome', ['primeiro_nome', 'segundo_nome'])

# Usando a Named Tuple:

aluno1 = exemplo3(primerio_nome='Gabriel', segundo_nome='Correa')

# Acessando os dados:

# Forma 1:
print(aluno1[0])

# Forma 2:
print(aluno1.primeiro_nome)

# Módulo Deque:

# Deque é uma lista de alta-performance

exemplo = deque('Gabriel')
