frase = input("Escribe una frase: ")
letra = input("Escribe una letra: ")
contador = 0
for caracter in frase:
    if caracter == letra:
        contador += 1
resultado = "La letra '{}' aparece {} veces en la frase".format(letra, contador)
print(resultado)