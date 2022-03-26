string1 = input("Digite uma frase: ")
string1 = list(string1.lower())

for indice, letra in enumerate(string1):
    if (indice % 2) == 1:
        letra = letra.upper()
        string1[indice] = letra
    else:
        letra = letra.lower()
        string1[indice] = letra


print("".join(string1))
