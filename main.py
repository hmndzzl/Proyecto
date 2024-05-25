#---------------------------------
# Algoritmos y Programación Básica
# Sección 170
# Diego Andre Calderon Salazar - 241263
# Hugo Roberto Méndez Lee - 241265
# Pedro Julio Caso Tzunún - 241286
# Marisabel Santizo Arenas - 241400
# Arodi Josué Chávez Ramírez - 241112
#---------------------------------

import funciones as f #Importar las funciones
import pandas as pd # Importar la librería de pandas

# Variables
menu1 = """
1 = Iniciar Sesión
2 = Crear Cuenta"""

menu2 = """
1 = Obtener Base de Datos
2 = Obtener Promedio Semanal
3 = Salir"""

menu3 = """
1 = Últimos Registrados
2 = Día específico
3 = Semanal 
"""
menu_promedios = """
¿Cuál dato quiere extraer el promedio semanal?

1 = pH
2 = Temperatura
3 = Humedad 
"""

usuarios = {"DIEGO": "diego2843", "HUGO": "24Huguin", "PEDRO": "Elpepe24", "MARISA": "Santizo32", "ARODI": "contraseña"}

datos = {
    "DIEGO": {"pH": [2.4, 2.9, 2.3, 2.1, 2.9, 1.6, 1.9], "Temperatura": [21, 25, 25, 23, 22, 25, 25], "Humedad": [64, 65, 57, 56, 55, 66, 57]},

    "HUGO": {"pH": [2.6, 1.5, 2.5, 2.5, 1.9, 1.6, 1.7], "Temperatura": [21, 23, 25, 24, 21, 22, 23], "Humedad": [58, 67, 56, 64, 68, 64, 52]},

    "PEDRO": {"pH": [2.1, 2.4, 1.8, 2.2, 2.7, 2.2, 1.4], "Temperatura": [25, 25, 20, 24, 24, 20, 20], "Humedad": [61, 64, 67, 59, 60, 64, 59]},

    "MARISA": {"pH": [1.5, 2.7, 1.7, 2.7, 2.5, 2.8, 2.4], "Temperatura": [21, 24, 23, 22, 22, 23, 25], "Humedad": [53, 64, 53, 62, 66, 60, 60]},

    "ARODI": {"pH": [1.9, 2.6, 2.5, 2.2, 2.9, 2.1, 2.9], "Temperatura": [25, 23, 20, 23, 23, 21, 24], "Humedad": [64, 53, 57, 63, 60, 52, 59]}
}


# Menú 1: Inicio de Sesión
opcion = f.menu(menu1, 2)

if opcion == 1:
    usuario = f.ingresar(usuarios)
    if not usuario:
        exit()

    
if opcion == 2:
    f.crear_usario(usuarios)
    usuario = f.ingresar(usuarios).upper()
    datos[usuario] = {"pH": [0, 0, 0, 0, 0, 0, 0], "Temperatura": [0, 0, 0, 0, 0, 0, 0], "Humedad": [0, 0, 0, 0, 0, 0, 0]}


# Segundo Menú: 
w = True
while w:
    opcion = f.menu(menu2, 3)
    
    if opcion == 1:
        print("obtener base de datos")
        opcion2 = f.menu(menu3, 3)

        # Últimos datos registrados
        if opcion2 == 1:
            print(f"Últimos datos registrados: ph: {datos[usuario]['pH'][-1]}, Temperatura: {datos[usuario]['Temperatura'][-1]}, Humedad: {datos[usuario]['Humedad'][-1]}%")

        if opcion2 == 2:
            f.obtener_datos_dia(datos[usuario])

        if opcion2 == 3:
            f.obtener_datos_semanales(datos[usuario])
        
    if opcion == 2: 
        opcion3 = f.menu(menu_promedios, 3)

        # Si el usuario escoge pH 
        if opcion3 == 1:
            prom_ph = f.promedio_ph(datos[usuario])
            print(f"El promedio de pH semanal es de: {prom_ph}")

        # Si el usuario escoge temperatura
        if opcion3 == 2:
            prom_temp = f.promedio_temp(datos[usuario])
            print(f"El promedio de temperaturas semanales es de: {prom_temp} grados centígrados")

        # Si el usuario escoge humedad
        if opcion3 == 3:
            prom_hum = f.promedio_humedad(datos[usuario])
            print(f"El promedio de porcentaje de humedad semanal es de: {prom_hum}%")
        
    if opcion == 3:
        print("Saliendo...")
        w = False
    
        
        
        
    
    