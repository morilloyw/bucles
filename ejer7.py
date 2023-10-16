contraseña_correcta = "contraseña"
contraseña_correcta_ingresada = False
while not contraseña_correcta_ingresada:
    contraseña_ingresada = input("Introduzca la contraseña: ")
    
    if contraseña_ingresada == contraseña_correcta:
        print("La contraseña es correcta!")
        contraseña_correcta_ingresada = True
    else:
        print("Contraseña incorrecta, intentelo de nuevo")
