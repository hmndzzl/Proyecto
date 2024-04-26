def crear_usario(usuarios):
    usuario = input("Ingrese nombre de usuario: ")
    contraseña_valida = False
    while contraseña_valida == False: 
        contraseña = input("Ingrese contraseña: ")
        contraseña2 = input("Ingrese de nuevo su contraseña: ")
        if contraseña == contraseña2:
            contraseña_valida = True
        else:
            print("Las contraseñas no coinciden, intente de nuevo")
    usuarios[usuario] = contraseña
    print(f"Usuario {usuario} creado exitosamente")

def ingresar(usuarios):
    usuario = input("Ingrese nombre de usuario: ")
    if usuario in usuarios:
        contraseña = input("Ingrese contraseña: ")
        if usuarios[usuario] == contraseña:
            print("Inicio de sesión exitoso")
        else:
            print("Contraseña incorrecta")
    else:
        print("El usuario no existe")

