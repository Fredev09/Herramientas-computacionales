# Importar librerias
import tkinter as tk
from tkinter import ttk

# Inicializar la ventana principal
ventana = tk.Tk()
ventana.title("Python - Tkinter")

# Agregar lista desplegable
numero = tk.StringVar()
seleccionar_numero = ttk.Combobox(ventana, width=12, textvariable=numero)

# Llenar la lista desplegable
seleccionar_numero['values'] = (1, 3, 5, 7, 11)

# Posicionar la lista desplegable
seleccionar_numero.grid(column=0, row=1)

# Elemento de la lista seleccionado por default
seleccionar_numero.current(0)

# Activar ventana
ventana.mainloop()