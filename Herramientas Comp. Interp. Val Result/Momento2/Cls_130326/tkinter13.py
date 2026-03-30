import tkinter as tk
from tkinter import ttk

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("400x300")  # Tamaño de la ventana
ventana.title("Ventana con dos Pestañas")  # Título de la ventana

# Crear el control de pestañas
tabControl = ttk.Notebook(ventana)

# Crear la primera pestaña
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

# Crear la segunda pestaña
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

# Empaquetar el control de pestañas
tabControl.pack(expand=1, fill="both")

# Ejecutar la ventana
ventana.mainloop()