cantidad = int(input("Cantidad a invertir (en euros): "))
interes_porcentaje = int(input("Interes anual (%): "))
años = int(input("Numero de años: "))
interes_decimal = interes_porcentaje / 100

for año in range(1, años + 1):
    cantidad += cantidad * interes_decimal
    print("Año {}: {} euros".format(año, cantidad))
print("Capital total después de {} años: {} euros".format(años, cantidad))
