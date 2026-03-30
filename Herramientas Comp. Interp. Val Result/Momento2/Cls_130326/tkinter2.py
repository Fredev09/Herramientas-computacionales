# Importar libreria
import tkinter as tk
from tkinter import ttk


def funcion_click():
    accion.configure(text='Hola ' + nombre.get())

# Inicializar ventana
ventana = tk.Tk()
ventana.title("Python - Tkinter")

# Agregar etiqueta por medio de un objeto
etiqueta = ttk.Label(ventana, text="Escribe tu nombre")
etiqueta.grid(column=0, row=0)

# Agregar una caja de texto
nombre = tk.StringVar()
preguntar_nombre = ttk.Entry(ventana, width=20, textvariable=nombre)
preguntar_nombre.grid(column=0, row=1)

# Agregar un boton
accion = ttk.Button(ventana, text="Haz Click Aqui!", command=funcion_click)
accion.grid(column=1, row=1)

# Activar ventana
ventana.mainloop()
