string1 = "Campus Code"
string1 = list(string1.lower())

for indice, letra in enumerate(string1):
    if (indice % 2) == 1:
        letra = letra.upper()
        print(letra, "Teste minuscula")
        string1[indice] = letra
    else:
        letra = letra.lower()
        print(letra, "Teste Maiuscula")
        string1[indice] = letra


print("".join(string1))
