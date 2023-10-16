numero = int(input("Escribe el numero entero positivo: "))
if numero <= 0:
    print("Vuleva a escribir un numero entero positivo")
else:
    impares = ""
    for i in range(1, numero + 1, 2):
        if i != 1:
            impares += ", "  
        impares += str(i)
    print("Estos son los numeros impares desde el 1", numero, ":", impares)