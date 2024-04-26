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

# Menú 1: Inicio de Sesión
w = True
while w:
    # Imprime menú 1 
    print(menu1)  
    opcion = input("Ingrese el número de la opción que desea: ")
    # Si el usuario ingresa un valor fuera del rango aceptado:
    while opcion not in range(1, 3):
        print("Ha ingresado un valor fuera de los aceptados, vuelva a intentarlo: ")
        print(menu1)  
        opcion = input("Ingrese el número de la opción que desea: ")
        
    
    