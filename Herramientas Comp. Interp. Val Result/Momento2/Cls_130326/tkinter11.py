import tkinter as tk
from tkinter import Menu  # Importar la biblioteca para hacer menús

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("400x300")  # Tamaño de la ventana
ventana.title("Ejemplo de Menú con Línea Divisoria")  # Título de la ventana

# Crear la barra del menú
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

# Agregar opciones al menú
opciones_menu = Menu(barra_menu)
opciones_menu.add_command(label="Nuevo")  # Opción "Nuevo"
opciones_menu.add_separator()  # Línea divisoria
opciones_menu.add_command(label="Salir")  # Opción "Salir"
barra_menu.add_cascade(label="Archivo", menu=opciones_menu)

# Ejecutar la ventana
ventana.mainloop()