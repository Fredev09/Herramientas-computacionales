import tkinter as tk

# Colores para los radiobuttons
COLOR1 = "red"
COLOR2 = "green"
COLOR3 = "blue"

# Inicializar ventana
ventana = tk.Tk()
ventana.title("Radiobuttons Tkinter")
ventana.geometry("300x200")

# Variable para guardar la opción seleccionada
opcion = tk.IntVar()

# Función para manejo de los botones
def funcion_radio():
    selector = opcion.get()
    if selector == 1:
        ventana.configure(background=COLOR1)
    elif selector == 2:
        ventana.configure(background=COLOR2)
    elif selector == 3:
        ventana.configure(background=COLOR3)

# Crear 3 Radiobuttons

# Radiobutton 1
radio1 = tk.Radiobutton(ventana, text=COLOR1, variable=opcion, value=1, command=funcion_radio)
radio1.grid(column=0, row=5, sticky=tk.W)

# Radiobutton 2
radio2 = tk.Radiobutton(ventana, text=COLOR2, variable=opcion, value=2, command=funcion_radio)
radio2.grid(column=1, row=5, sticky=tk.W)

# Radiobutton 3
radio3 = tk.Radiobutton(ventana, text=COLOR3, variable=opcion, value=3, command=funcion_radio)
radio3.grid(column=2, row=5, sticky=tk.W)

# Activar ventana
ventana.mainloop()