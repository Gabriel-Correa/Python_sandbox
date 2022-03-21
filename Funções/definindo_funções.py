# Definindo funções

# Pequenos trechos de códigos que realizam tarefas específicas;
# Pode ou não receber parâmetros e retornar um dado;


# Utilizando funções:

cores = ['verde', 'vermelho', 'azul', 'branco']

# Função integrada(Built-in)

print(cores)  # a função print é integrada à linguagem python

# Para definir uma função em python, usamos def(definição), o nome da função, os parâmetros que serão recebidos e finalizada com ':'


def nome_funcao(parametros):
    print(parametros)

# OBS: ao seguir o PEP8, usamos snake case para nomear funções, iniciando com letra minuscula e separando as palavras com underline(_)
# OBS: Parâmetros são opcionais, caso haja mais de um, separe-os por ',' (parametro1, parametro2)


# Para executar a função, basta digitar seu nome e finalizar com ()

# Ao utilizar o "Olá mundo" como parametro, a função irá printar esta string
nome_funcao("Olá mundo")
