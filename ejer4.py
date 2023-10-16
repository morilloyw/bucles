numero = int(input("Escribir un numero entero positivo: "))
if numero < 0:
    print("El numero escrito no es positivo.")
else:
    cuenta_atras = ""
    for i in range(numero, -1, -1):
        if cuenta_atras == "":
            cuenta_atras = str(i)
        else:
            cuenta_atras = cuenta_atras + ", " + str(i)
    print("Cuenta atras:", cuenta_atras)