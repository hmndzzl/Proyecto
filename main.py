#---------------------------------
# Algoritmos y Programación Básica
# Sección 170
# Diego Andre Calderon Salazar - 241263
# Hugo Roberto Méndez Lee - 241265
# Pedro Julio Caso Tzunún - 241286
# Marisabel Santizo Arenas - 241400
# Arodi Josué Chávez Ramírez - 241112
#---------------------------------

import funciones as f

# Variables
menu1 = """
1 = Iniciar Sesión
2 = Crear Cuenta"""

menu2 = """
1 = Obtener Base de Datos
2 = Prueba
3 = Salir"""

menu3 = """
1 = Hoy
2 = Semanal 
"""

datos = {"pH": [2.3, 3.1, 3.3, 2.2, 1.5, 1.2, 2.1], "Temperatura": [20, 22, 21, 24, 26, 25, 22], "Humedad": [55, 56, 57, 68, 50, 67, 70]}

usuarios = {"DIEGO": "diego2843", "HUGO": "24Huguin", "PEDRO": "Elpepe24", "MARISA": "Santizo32", "ARODI": "contraseña"}


# Función que imprime un menú y recibe como argumentos el string con el menú y la cantidad de opciones que tiene le menú. 
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


# Menú 1: Inicio de Sesión
opcion = menu(menu1, 2)

if opcion == 1:
    f.ingresar(usuarios)
    
if opcion == 2:
    print("función de crear una cuenta")
    print("función para iniciar sesión")

# Segundo Menú: 
w = True
while w:
    opcion = menu(menu2, 3)
    
    if opcion == 1:
        print("obtener base de datos")
        opcion2 = menu(menu3, 2)

        # Datos de hoy
        if opcion2 == 1:
            print(datos[-1])

        if opcion2 == 2:
            f.obtener_datos_semanales(datos)
        
    if opcion == 2: 
        print("prueba prueba")
        
    if opcion == 3:
        print("Saliendo...")
        w = False
    
        
        
        
    
    