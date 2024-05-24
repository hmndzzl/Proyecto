
# Función que imprime un menú y recibe como argumentos el string con el menú y la cantidad de opciones que tiene le menú. 
def menu(menu, opciones):
    control = False
    while control == False:
        # Imprime menú  
        print(menu)  
        opcion = input("Ingrese el número de la opción que desea: ")
        # Si el usuario ingresa un valor fuera del rango aceptado:
        try : 
            int(opcion)
        except ValueError:
            print("Error, ingrese una opción válida. ")
        else:
            while opcion not in list(range(1, opciones + 1)):
                print("Ha ingresado un valor fuera de los aceptados, vuelva a intentarlo:")
                print(menu)  
                opcion = int(input("Ingrese el número de la opción que desea: "))
                control = True
            return opcion

# Función para Crear un nuevo usuario
def crear_usario(usuarios):
    usuario_valido = False
    while usuario_valido == False:
        usuario = input("Ingrese nombre de usuario: ").upper()
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

# Función para iniciar sesión en un usuario existente
def ingresar(usuarios):
    ingreso = False
    while ingreso == False:
        usuario = input("Ingrese nombre de usuario: ").upper()
        if usuario in usuarios:
            contraseña = input("Ingrese contraseña: ")
            if usuarios[usuario] == contraseña:
                print("Inicio de sesión exitoso")
                ingreso = True
            else:
                print("Contraseña incorrecta")
        else:
            print("El usuario no existe")

    return usuario

# Función para obtener los datos en una semana completa 
def obtener_datos_semanales(datos):
    index = 0
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for i in range(0,7):
        print(f"Datos día {dias[index]}: ph: {datos['pH'][index]}, Temperatura: {datos['Temperatura'][index]}, Humedad: {datos['Humedad'][index]}%")
        index += 1


# Función Para obtener los datos en un día específico de la semana
def obtener_datos_dia(datos):
    dias = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]

    dia = input("¿De qué día de la semana quiere saber los datos? ").upper()

    index = dias.index(dia)
    
    ph = datos["pH"][index]
    temperatura = datos["Temperatura"][index]
    humedad = datos["Humedad"][index]
    print(f"Datos día {dias[index].capitalize()}: ph: {ph}, Temperatura: {temperatura}, Humedad: {humedad}%")

#Función para obtener el promedio del pH
def promedio_ph(datos):
    suma = 0
    total = 0
    for i in datos["pH"]:
        suma += i
        total += 1
    
    return suma / total

#Función para obtener el promedio de la temperatura
def promedio_temp(datos):
    suma = 0
    total = 0
    for i in datos["Temperatura"]:
        suma += i
        total += 1
    
    return suma / total

#Función para obtener el promedio de la humedad
def promedio_humedad(datos):
    suma = 0
    total = 0
    for i in datos["Humedad"]:
        suma += i
        total += 1
    
    return suma / total





