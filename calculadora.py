
numero1 = int(input("Qual o primeiro número?"))
numero2 = int(input("Qual o segundo número?"))
fator_matematico = input("O que deseja fazer com estes números?")


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def multiplicacao(num1, num2):
    return num1 * num2


def divisao(numerador, divisor):
    return numerador / divisor


def calculadora(primeiro_numero, segundo_numero, funcao=soma):
    return funcao(primeiro_numero, segundo_numero)


if fator_matematico == 'Somar':
    resultado = calculadora(numero1, numero2, soma)
    print(f'A soma dos números {numero1} e {numero2} é {resultado}')
elif fator_matematico == "Subtrair":
    resultado = calculadora(numero1, numero2, subtracao)
    print(f'A subtração dos números {numero1} e {numero2} é {resultado}')
elif fator_matematico == "Multiplicar":
    resultado = calculadora(numero1, numero2, multiplicacao)
    print(f'A multiplicação entre os números {numero1} e {numero2} é {resultado}')
elif fator_matematico == "Dividir":
    while numero2 == 0:
        print("Impossível dividr por zero!")
        numero2 = int(input('Selecione outro número: '))
    resultado = calculadora(numero1, numero2, divisao)
    print(f'A divisão entre os números {numero1} e {numero2} é {resultado}')

