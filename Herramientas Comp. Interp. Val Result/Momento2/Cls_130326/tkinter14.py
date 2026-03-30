import tkinter as tk
from tkinter import Menu, messagebox as mBox  # Importar las bibliotecas necesarias

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("400x300")  # Tamaño de la ventana
ventana.title("Ejemplo de Menú y Caja de Mensaje")  # Título de la ventana

# Función para el manejo del evento (mostrar el mensaje)
def funcion_caja_mensaje():
    mBox.showinfo('Mensaje de Python en una caja de mensajes', 
                  'Esta interfaz fue creada con tkinter\nFebrero 2020.')

# Crear la barra del menú
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

# Crear un menú (Ayuda)
menu_ayuda = Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=funcion_caja_mensaje)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# Ejecutar la ventana
ventana.mainloop()