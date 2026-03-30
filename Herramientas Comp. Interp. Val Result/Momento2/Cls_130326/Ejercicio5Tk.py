#Crear una ventana con Tkinter
from tkinter import* #llama a toda la librería tkinter
# Configurar la ventana principal root
root = Tk()#Instanciamos pantalla principal
root.title('Calculadora') #Título de la ventana
root.geometry('270x130') #Configuramos el Ancho x Altura de la ventana
root.config(bg="gray90") #Fondo de la ventana
#root.iconbitmap("icono.ico") #Llamamos al archivo de tipo ico
#Función con parámetros
def calculadora(x):
    num_1 = float(entrada_1.get()) #Se obtiene el valor Entry (siempre es string)
    num_2 = float(entrada_2.get())
    if x==1: #suma
        res = num_1 + num_2
    elif x==2: #resta
        res = num_1 - num_2
    elif x==3: #multiplicacion
        res =  num_1*num_2
    elif x==4: #division
        res =  num_1/num_2
    label_0['text'] = res
#Creamos los frames, etiquetas, entradas y botones
fm1 = Frame(root,padx=5,pady=5) #Frame 1
label_0 = Label(fm1,bd=1,width=26,height=2,bg="gray90",relief="sunken",font="calibri 14 bold")
fm2 = Frame(root) #Frame 2
label_1 = Label(fm2, text="Ingresa 1° número")
label_2 = Label(fm2, text="Ingresa 2° número")
entrada_1 = Entry(fm2, font="calibri 12")
entrada_2 = Entry(fm2, font="calibri 12")
fm3=Frame(root) #Frame 3
boton_1=Button(fm3,text="SUMAR",fg="white",bg="gray35",font="calibri 11 bold",command=lambda:calculadora(1))
boton_2=Button(fm3,text="RESTAR",fg="white",bg="gray35",font="calibri 11 bold",command=lambda:calculadora(2))
boton_3=Button(fm3,text="MULTIPLICAR",fg="white",bg="gray35",font="calibri 11 bold",command=lambda:calculadora(3))
boton_4=Button(fm3,text="DIVIDIR",fg="white",bg="gray35",font="calibri 11 bold",command=lambda:calculadora(4))
#Posicionamiento
fm1.pack(side=TOP) #Posicionamiento relativo (pack)
label_0.pack() #Posicionamiento relativo (pack)
fm2.pack(side=TOP,) #Posicionamiento relativo (pack)
label_1.grid(row=0, column=0) #Posicionamiento tipo grilla (grid)
entrada_1.grid(row=0, column=1) #Posicionamiento tipo grilla (grid)
label_2.grid(row=1, column=0) #Posicionamiento tipo grilla (grid)
entrada_2.grid(row=1, column=1) #Posicionamiento tipo grilla (grid)
fm3.pack(side=TOP,) #Posicionamiento relativo (pack)
boton_1.pack(side=LEFT, expand=True) #Posicionamiento relativo (pack)
boton_2.pack(side=LEFT, expand=True) #Posicionamiento relativo (pack)
boton_3.pack(side=LEFT, expand=True) #Posicionamiento relativo (pack)
boton_4.pack(side=LEFT, expand=True) #Posicionamiento relativo (pack)
root.mainloop() #Bucle que actualiza continuamente la ventana