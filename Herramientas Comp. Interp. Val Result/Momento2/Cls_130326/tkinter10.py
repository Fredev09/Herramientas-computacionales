import tkinter as tk
from tkinter import ttk

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("400x300")  # Tamaño de la ventana
ventana.title("Ejemplo de LabelFrame")  # Título de la ventana

# Crear un contenedor para almacenar componentes
contenedor = ttk.LabelFrame(ventana, text='Etiquetas en un contenedor')
contenedor.grid(column=0, row=7)

# Etiquetas dentro del contenedor
ttk.Label(contenedor, text="Etiqueta1").grid(column=0, row=0)
ttk.Label(contenedor, text="Etiqueta2").grid(column=1, row=0)
ttk.Label(contenedor, text="Etiqueta3").grid(column=2, row=0)

# Ejecutar la ventana
ventana.mainloop()