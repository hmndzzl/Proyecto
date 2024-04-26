def crear_usario(usuarios):
    usuario_valido = False
    while usuario_valido == False:
        usuario = input("Ingrese nombre de usuario: ")
        if usuario in usuarios.keys():
            print("Error el usuario ya está tomado.")
        else: 
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
            usuario_valido = True

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

def obtener_datos(datos):
    index = 0
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for i in range(0,7):
        try:
            ph = datos["pH"][index]
        except IndexError:
            ph = "N.D"
        try:
            temperatura = datos["Temperatura"][index]
        except IndexError:
            temperatura = "N.D."
        try:
            humedad = datos["Humedad"][index]
        except IndexError:
            humedad = "N.D."
        print(f"Datos día {dias[index]}: ph: {ph}, Temperatura: {temperatura}, Humedad: {humedad}%")
        index += 1

        
items = {"pH": [1, 2, 3, 4, 5, 6, 7], "Temperatura": [1, 2, 3, 4, 5, 6], "Humedad": [1, 2, 4, 5, 6, 7]}
obtener_datos(items)