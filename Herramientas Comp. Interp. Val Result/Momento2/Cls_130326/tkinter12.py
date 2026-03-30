import tkinter as tk
from tkinter import Menu  # Importar la biblioteca para hacer menús

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("400x300")  # Tamaño de la ventana
ventana.title("Ejemplo de Menú con 2 Opciones")  # Título de la ventana

# Crear la barra del menú
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

# Opción 1: Menú Archivo
menu_archivo = Menu(barra_menu)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir")
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Opción 2: Menú Ayuda
menu_ayuda = Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de")
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# Ejecutar la ventana
ventana.mainloop()