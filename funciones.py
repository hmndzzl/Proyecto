# Función que imprime un menú y recibe como argumentos el string con el menú y la cantidad de opciones que tiene le menú. 
def menu(menu_text, opciones):
    while True:
        # Imprime el menú
        print(menu_text)
        opcion = input("Ingrese el número de la opción que desea: ")
        
        # Verifica si la opción ingresada es un número válido
        try:
            opcion = int(opcion)
            if 1 <= opcion <= opciones:
                return opcion
            else:
                print(f"Error, ingrese un número entre 1 y {opciones}.")
        except ValueError:
            print("Error, ingrese un número válido.")

def ingresar_datos():
    valido = False
    print("¿Desea agregar datos? Si: 1 | No: 2")
    
    while not valido:
        dato = {}
        dato["pH"] = []
        dato["Temperatura"] = []
        dato["Humedad"] = []
        agregar_datos = input("Ingrese el número de opción: ")
        
        if agregar_datos == "1":
            dias_semana = {1: "lunes", 2: "martes", 3: "miércoles", 4: "jueves", 5: "viernes", 6: "sábado", 7: "domingo"}
            for i in dias_semana:
                print(f"Ingrese el pH del día: {dias_semana[i]}")
                ph = input("Ingrese el valor: ")
                print(f"Ingrese la temperatura del día: {dias_semana[i]}")
                temperatura = input("Ingrese el valor: ")
                print(f"Ingrese la humedad del día: {dias_semana[i]}")
                humedad = input("Ingrese el valor: ")
                try: 
                    ph = float(ph)
                    temperatura = float(temperatura)
                    humedad = float(humedad)
                    
                    dato["pH"].append(ph)
                    dato["Temperatura"].append(temperatura)
                    dato["Humedad"].append(humedad)
                    valido = True

                except ValueError:
                    print("Error, ingrese valores numéricos válidos para pH, temperatura y humedad.")

        elif agregar_datos == "2":
            print("Se añadirán datos por defecto.")
            dato = {"pH": [0, 0, 0, 0, 0, 0, 0], "Temperatura": [0, 0, 0, 0, 0, 0, 0], "Humedad": [0, 0, 0, 0, 0, 0, 0]}
            valido = True

        else: 
            print("Error, ingrese una opción válida") 

    return dato



# Función para Crear un nuevo usuario
def crear_usario(usuarios_df, usuarios, datos):
    usuario_valido = False
    while usuario_valido == False:
        usuario = input("Ingrese nombre de usuario: ").upper()
        if (usuarios_df['Usuario'] == usuario).any():  # Retorna True si el usuario existe en el DataFrame 
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
            añadir = ingresar_datos()
            datos[usuario] = añadir
            print(f"Usuario {usuario} creado exitosamente")
            usuario_valido = True
    return usuario

# Función para iniciar sesión en un usuario existente
def ingresar(usuarios_df, usuarios, datos):
    ingreso = False
    while ingreso == False:
        usuario = input("Ingrese nombre de usuario: ").upper()
        if (usuarios_df['Usuario'] == usuario).any():  # Retorna True si el usuario existe en el DataFrame 
            contraseña = input("Ingrese contraseña: ")
            if contraseña == usuarios_df.loc[usuarios_df['Usuario'] == usuario, 'Contraseña'].values[0]:
                print("Inicio de sesión exitoso")
                ingreso = True
                return usuario
            else:
                print("Contraseña incorrecta")
        else:
            w = False
            while w == False:
                print("El usuario no existe")
                opcion = input("¿Desea crear un nuevo usuario? (sí/no): ").lower()
                if opcion == 'sí' or opcion == 'si':
                    crear_usario(usuarios_df, usuarios, datos)
                    w = True
                    return usuario
                else:
                    print("Error, el programa terminará debido a que no se pudo validar el usuario.")
                    w = True
                ingreso = True              

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

