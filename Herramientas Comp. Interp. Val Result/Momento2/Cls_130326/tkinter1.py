# Importar libreria
import tkinter as tk
from tkinter import ttk


def funcion_click():
    # Cambie "Haz" por "Has" (del verbo haber) y quite la tilde
    accion.configure(text="** Has hecho Click! **")
    etiqueta.configure(foreground='red')


# Inicializar ventana
ventana = tk.Tk()
ventana.title("Python - Tkinter")

# Agregar etiqueta por medio de un objeto
etiqueta = ttk.Label(ventana, text="Hola Crayola!!!")
etiqueta.grid(column=0, row=0)

# Agregar un boton
accion = ttk.Button(ventana, text="Haz Click Aqui!", command=funcion_click)
accion.grid(column=1, row=0)

# Activar ventana
ventana.mainloop()
