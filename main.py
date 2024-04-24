import tkinter as tk

def saludar():
    label_saludo.config(text="¡Hola, Mundo!")

root = tk.Tk()
root.title("Mi Aplicación")
root.geometry("800x500")

# Etiqueta
label_saludo = tk.Label(root, text="¡Bienvenido!")
label_saludo.pack(pady=20)  # pady es el espacio vertical alrededor del widget

# Botón
boton_saludar = tk.Button(root, text="Saludar", command=saludar)
boton_saludar.pack()

root.mainloop()

# prueba de nuevo