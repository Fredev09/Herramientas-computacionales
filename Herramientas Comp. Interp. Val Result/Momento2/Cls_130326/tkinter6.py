# Importar librería
import tkinter as tk
from tkinter import ttk

# Importar librería para los menús
from tkinter import Menu

# Importar librería para las cajas de mensajes
from tkinter import messagebox as mBox

def funcion_caja_mensaje():
    mBox.showinfo('Mensaje de Python en una caja de mensajes',
                  'Esta interface fué creada con tkinter\nFebrero 2020.')

# Inicializar ventana
ventana = tk.Tk()
ventana.title("Python - Tkinter")

# Crear la barra del menú
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

# Agregar un menú
menu_ayuda = Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=funcion_caja_mensaje)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# Activar ventana
ventana.mainloop()