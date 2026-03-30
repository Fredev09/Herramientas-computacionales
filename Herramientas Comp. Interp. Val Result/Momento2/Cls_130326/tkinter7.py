import tkinter as tk  # Importamos la librería tkinter

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("400x300")  # Configuramos el tamaño de la ventana
ventana.title("Ejemplo de Checkbuttons")  # Título de la ventana

# Checkbutton de 3 opciones

# Casilla 1: Deshabilitada ("Disabled")
opcion_1 = tk.IntVar()
casilla_1 = tk.Checkbutton(ventana, text="Leer", variable=opcion_1, state='disabled')
casilla_1.select()
casilla_1.grid(column=0, row=4, sticky=tk.W)

# Casilla 2: No seleccionada ("deselect")
opcion_2 = tk.IntVar()
casilla_2 = tk.Checkbutton(ventana, text="Ver películas", variable=opcion_2)
casilla_2.deselect()
casilla_2.grid(column=1, row=4, sticky=tk.W)

# Casilla 3: Seleccionada ("select")
opcion_3 = tk.IntVar()
casilla_3 = tk.Checkbutton(ventana, text="Redes Sociales", variable=opcion_3)
casilla_3.select()
casilla_3.grid(column=2, row=4, sticky=tk.W)

# Función para mostrar los valores de las opciones seleccionadas
def mostrar_selecciones():
    seleccion_1 = "Seleccionado" if opcion_1.get() else "No seleccionado"
    seleccion_2 = "Seleccionado" if opcion_2.get() else "No seleccionado"
    seleccion_3 = "Seleccionado" if opcion_3.get() else "No seleccionado"
    
    etiqueta_resultado.config(text=f"Opción 1: {seleccion_1}\nOpción 2: {seleccion_2}\nOpción 3: {seleccion_3}")

# Botón para mostrar el estado de las casillas
boton_mostrar = tk.Button(ventana, text="Mostrar Selección", command=mostrar_selecciones)
boton_mostrar.grid(column=0, row=5, columnspan=3)

# Etiqueta para mostrar los resultados
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_resultado.grid(column=0, row=6, columnspan=3)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()