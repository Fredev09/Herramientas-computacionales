import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos


class FormularioArticulos:
    def __init__(self):

        # Instancia de la clase Articulos
        self.articulo1 = articulos.Articulos()

        # Ventana principal
        self.ventana1 = tk.Tk()
        self.ventana1.title("Mantenimiento de artículos")

        # Notebook (pestañas)
        self.cuaderno1 = ttk.Notebook(self.ventana1)

        self.carga_articulos()
        self.modificar_articulos()
        self.consulta_por_codigo()
        self.listado_completo()

        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)

        self.ventana1.mainloop()

    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")

        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Artículo")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe1, text="Descripción:").grid(
            column=0, row=0, padx=4, pady=4)
        self.descripcioncarga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga).grid(
            column=1, row=0, padx=4, pady=4)

        ttk.Label(self.labelframe1, text="Precio:").grid(
            column=0, row=1, padx=4, pady=4)
        self.preciocarga = tk.StringVar()
        ttk.Entry(self.labelframe1, textvariable=self.preciocarga).grid(
            column=1, row=1, padx=4, pady=4)

        ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar).grid(
            column=1, row=2, padx=4, pady=4)

    def modificar_articulos(self):
        self.pagina_modificar = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina_modificar, text="Modificar articulos")

        self.labelframe_modificar = ttk.LabelFrame(
            self.pagina_modificar, text="Artículo")
        self.labelframe_modificar.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe_modificar, text="ID:").grid(
            column=0, row=0, padx=4, pady=4)
        self.idmod = tk.StringVar()
        ttk.Entry(self.labelframe_modificar, textvariable=self.idmod).grid(
            column=1, row=0, padx=4, pady=4)

        ttk.Label(self.labelframe_modificar, text="Descripción:").grid(
            column=0, row=1, padx=4, pady=4)
        self.descripcionmod = tk.StringVar()
        ttk.Entry(self.labelframe_modificar, textvariable=self.descripcionmod).grid(
            column=1, row=1, padx=4, pady=4)

        ttk.Label(self.labelframe_modificar, text="Precio:").grid(
            column=0, row=2, padx=4, pady=4)
        self.preciomod = tk.StringVar()
        ttk.Entry(self.labelframe_modificar, textvariable=self.preciomod).grid(
            column=1, row=2, padx=4, pady=4)

        ttk.Button(self.labelframe_modificar, text="Modificar",
                   command=self.modificar).grid(column=1, row=3, padx=4, pady=4)
        ttk.Button(self.labelframe_modificar, text="Limpiar",
                   command=self.limpiar).grid(column=1, row=4, padx=4, pady=4)
        ttk.Button(self.labelframe_modificar, text="Buscar",
                   command=self.buscar).grid(column=0, row=3, padx=4, pady=4)
        ttk.Button(self.labelframe_modificar, text="Eliminar",
                   command=self.eliminar).grid(column=0, row=4, padx=4, pady=4)

    def agregar(self):
        datos = (self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.descripcioncarga.set("")
        self.preciocarga.set("")

    def modificar(self):
        datos = (self.descripcionmod.get(), self.preciomod.get(), self.idmod.get())
        self.articulo1.modificar(datos)
        mb.showinfo("Información", "Los datos fueron modificados")
        self.idmod.set("")
        self.descripcionmod.set("")
        self.preciomod.set("")


    def limpiar(self):
        self.idmod.set("")
        self.descripcionmod.set("")
        self.preciomod.set("")


    def buscar(self):
        codigo = self.idmod.get()
        datos = self.articulo1.consulta((codigo,))

        if len(datos) > 0:
            self.descripcionmod.set(datos[0][0])
            self.preciomod.set(datos[0][1])
        else:
            mb.showinfo("Información", "No existe un artículo con ese código")
            self.descripcionmod.set("")
            self.preciomod.set("")


    def eliminar(self):
        codigo = self.idmod.get()
        if codigo == "":
            mb.showinfo("Información", "Ingrese un código para eliminar")
        else:
            self.articulo1.eliminar((codigo,))
            mb.showinfo("Información", "Artículo eliminado")
            self.idmod.set("")
            self.descripcionmod.set("")
            self.preciomod.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")

        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        ttk.Label(self.labelframe2, text="Código:").grid(
            column=0, row=0, padx=4, pady=4)
        self.codigo = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.codigo).grid(
            column=1, row=0, padx=4, pady=4)

        ttk.Label(self.labelframe2, text="Descripción:").grid(
            column=0, row=1, padx=4, pady=4)
        self.descripcion = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.descripcion,
                  state="readonly").grid(column=1, row=1, padx=4, pady=4)

        ttk.Label(self.labelframe2, text="Precio:").grid(
            column=0, row=2, padx=4, pady=4)
        self.precio = tk.StringVar()
        ttk.Entry(self.labelframe2, textvariable=self.precio,
                  state="readonly").grid(column=1, row=2, padx=4, pady=4)

        ttk.Button(self.labelframe2, text="Consultar", command=self.consultar).grid(
            column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos = (self.codigo.get(),)
        respuesta = self.articulo1.consulta(datos)

        if len(respuesta) > 0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set("")
            self.precio.set("")
            mb.showinfo("Información",
                        "No existe un artículo con dicho código")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")

        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        ttk.Button(self.labelframe3, text="Listado completo",
                   command=self.listar).grid(column=0, row=0, padx=4, pady=4)

        self.scrolledtext1 = st.ScrolledText(
            self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)

    def listar(self):
        respuesta = self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)

        for fila in respuesta:
            self.scrolledtext1.insert(
                tk.END,
                "Código: " + str(fila[0]) +
                "\nDescripción: " + fila[1] +
                "\nPrecio: " + str(fila[2]) + "\n\n"
            )


# Ejecutar aplicación
aplicacion1 = FormularioArticulos()
