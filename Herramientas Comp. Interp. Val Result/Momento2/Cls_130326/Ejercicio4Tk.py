#Crear una ventana con Tkinter
from tkinter import* #llama a toda la librería tkinter
# Configurar la ventana
root = Tk() #Instanciamos
root.geometry("400x200") #Configuramos el Ancho x Altura de la ventana
root.title("Tecsup") #Título de la ventana
root.config(bg="Pink") #Fondo de la ventana
#root.iconbitmap("asarco.ico") #Llamamos al archivo de tipo ico
#Creamos una etiqueta y entrada
label_1 = Label(root, text="Hola Mecatrónico", bg="black", fg="white",
font="curier 18 bold")
entry_1 = Entry(root)
boton_1 = Button(root, text="Boton")
#Posicionamiento grilla (grid)
label_1.place(x=0, y=0)
entry_1.place(x=0, y=0)
boton_1.place(x=0, y=0)
#Bucle que actualiza continuamente la ventana
root.mainloop()