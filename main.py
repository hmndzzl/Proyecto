#---------------------------------
# Algoritmos y Programación Básica
# Sección 170
# Diego Andre Calderon Salazar - 241263
# Hugo Roberto Méndez Lee - 241265
# Pedro Julio Caso Tzunún - 241286
# Marisabel Santizo Arenas - 241400
# Arodi Josué Chávez Ramírez - 241112
#---------------------------------

# Variables
menu1 = """
1 = Iniciar Sesión
2 = Crear Cuenta"""

menu2 = """
1 = Obtener Base de Datos Semanal
2 = """

# Función que imprime un menú y recibe como argumentos el string con el menú y la cantidad de opciones que tiene le menú. 
def menu(menu, opciones):
    # Imprime menú  
    print(menu)  
    opcion = int(input("Ingrese el número de la opción que desea: "))
    # Si el usuario ingresa un valor fuera del rango aceptado:
    while opcion not in list(range(1, opciones)):
        print("Ha ingresado un valor fuera de los aceptados, vuelva a intentarlo:")
        print(menu)  
        opcion = int(input("Ingrese el número de la opción que desea: "))
    return opcion


# Menú 1: Inicio de Sesión
w = True
while w:
    
    opcion = menu(menu1, 2)
    
    if opcion == 1:
        print("función de iniciar sesión")
        
    if opcion == 2:
        print("función de crear una cuenta")
        print("función para iniciar sesión")
    
    # Segundo Menú: 
    t = True    
   # while t:
        
        
        
        
    
    