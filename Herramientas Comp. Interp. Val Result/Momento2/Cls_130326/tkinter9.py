import tkinter as tk  # Importamos la librería tkinter
from tkinter import scrolledtext  # Importamos la librería para cajas de texto con desplazamiento

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("400x300")  # Configuramos el tamaño de la ventana
ventana.title("Ejemplo de Caja de Texto")  # Título de la ventana

# Configurar la caja de texto
scrol_ancho = 30
scrol_alto = 3

# Agregar la caja de texto
caja = scrolledtext.ScrolledText(ventana, width=scrol_ancho, height=scrol_alto, wrap=tk.WORD)
caja.grid(column=0, columnspan=3)  # Posicionamos la caja de texto en la ventana

# Agregar un texto de ejemplo a la caja de texto
caja.insert(tk.END, "Este es un ejemplo de caja de texto con desplazamiento.\nPuedes escribir varias líneas aquí.")

# Ejecutar el bucle principal de la ventana
ventana.mainloop()