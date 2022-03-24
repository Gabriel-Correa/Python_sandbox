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
# =====================================================================================================================================================

# Funções com retorno

# É possível que a função retorne um valor após seu processamento, para isso, devemos utilizar o comando return.


def funcao_com_retorno():
    return 7+7

# OBS: Para que haja o retorno da função, não necessariamente precisamos guardá-la em uma variável.

# A palvra return finaliza a função, ou seja, ao retornar o valor, é findada a execução do código interno
# Podemos retornar qualquer tipo de dado e múltiplos valores

# É possível haver mais de um return na função:


def funcao_multiplos_return(a):
    if a == 0:
        return 'True'
    else:
        return 'False'

# =====================================================================================================================================================

# Funções com parâmetro

# Parâmetros são dados que a função irá receber para processar

# É possível ter mais de um parâmetro


def funcao_com_parametro(a, b):
    return a+b

# Diferença entre parâmetros e argumentos:
# Parâmetros são as variáveis declaradas ao definir um função;
# Argumentos são dados passados durante a execução da função;

# OBS: A ordem dos parâmetros é extremamente importante;


def funcao(numerador, divisor):
    # Para que o calculo seja o esperado, deveremos informar primeiramente o numerador e após o divisor
    return numerador/divisor


# Argumentos nomeados(Keyword Arguments):
# Ao informar o nome do parâmetro nos argumentos, não importará a ordem dos fatores

print(funcao(divisor=4, numerador=4))


# Funções com parâmetro padrão

# Funções em que receber um parâmetro não é obrigatório

# ao alocar um valor no parametro, este passa a ser opcional, utilizando o valor alocado como padrão
def funcao_com_parametro_padrao(numero, potencia=2):
    return numero ** potencia

# OBS: Os parâmetros padrões devem ser declarados por último, conforme exemplo acima, do contrário, a função gerará erro.
