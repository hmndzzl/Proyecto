
def menu(menu, opciones):
    # Imprime menú  
    print(menu)  
    opcion = int(input("Ingrese el número de la opción que desea: "))
    # Si el usuario ingresa un valor fuera del rango aceptado:
    while opcion not in list(range(1, opciones + 1)):
        print("Ha ingresado un valor fuera de los aceptados, vuelva a intentarlo:")
        print(menu)  
        opcion = int(input("Ingrese el número de la opción que desea: "))
    return opcion

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

def obtener_datos_semanales(datos):
    index = 0
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for i in range(0,7):
        ph = datos["pH"][index]
        temperatura = datos["Temperatura"][index]
        humedad = datos["Humedad"][index]
        print(f"Datos día {dias[index]}: ph: {ph}, Temperatura: {temperatura}, Humedad: {humedad}%")
        index += 1

        
items = {"pH": [None, 2, 3, 4, 5, 6, 7], "Temperatura": [1, 2, 3, 4, 5, 6, None], "Humedad": [1, 2, None, 4, 5, 6, 7]}
obtener_datos_semanales(items)

