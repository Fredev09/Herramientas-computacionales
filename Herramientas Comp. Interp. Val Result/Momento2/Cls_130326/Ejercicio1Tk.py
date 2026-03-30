#Crear una ventana con Tkinter
from tkinter import* #llama a toda la librería tkinter
# Configurar la ventana
root = Tk() #Instanciamos
root.geometry("400x200") #Configuramos el Ancho x Altura de la ventana
root.title("Tecsup") #Título de la ventana
root.config(bg="green") #Fondo de la ventana
#root.iconbitmap("asarco.ico") #Llamamos al archivo de tipo ico
#Creamos una etiqueta
label_1 = Label(root, text="Hola estudiante", bg="black", fg="white", font="curier 18 bold")
#Posicionamos La etiqueta con el método pack
label_1.pack(expand=True)
root.mainloop()#Bucle que actualiza continuamente la venta