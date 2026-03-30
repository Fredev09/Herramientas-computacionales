import tkinter as tk

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("400x400")  # Tamaño de la ventana
ventana.title("Formulario de registro")  # Título de la ventana
ventana.config(bg="#34495E")  # Fondo oscuro para la ventana

# Título
titulo = tk.Label(ventana, text="Lenguajes de Programación", fg="white", bg="#3498DB", font=("Arial", 16, "bold"))
titulo.pack(fill=tk.X)

# Etiquetas y campos de texto
username_label = tk.Label(ventana, text="Username", fg="white", bg="#34495E", font=("Arial", 10))
username_label.place(x=22, y=60)
username_entry = tk.Entry(ventana, font=("Arial", 12))
username_entry.place(x=150, y=60, width=200)

password_label = tk.Label(ventana, text="Password", fg="white", bg="#34495E", font=("Arial", 10))
password_label.place(x=22, y=100)
password_entry = tk.Entry(ventana, show="*", font=("Arial", 12))
password_entry.place(x=150, y=100, width=200)

fullname_label = tk.Label(ventana, text="Fullname", fg="white", bg="#34495E", font=("Arial", 10))
fullname_label.place(x=22, y=140)
fullname_entry = tk.Entry(ventana, font=("Arial", 12))
fullname_entry.place(x=150, y=140, width=200)

age_label = tk.Label(ventana, text="Age", fg="white", bg="#34495E", font=("Arial", 10))
age_label.place(x=22, y=180)
age_entry = tk.Entry(ventana, font=("Arial", 12))
age_entry.place(x=150, y=180, width=200)

# Función para enviar los datos
def send_data():
    print("Username:", username_entry.get())
    print("Password:", password_entry.get())
    print("Fullname:", fullname_entry.get())
    print("Age:", age_entry.get())

# Botón para enviar la información
submit_btn = tk.Button(ventana, text="Grabar Información", fg="white", bg="#3EA8EF", width=30, height=2, font=("Arial", 10, "bold"), command=send_data)
submit_btn.place(x=80, y=220)
for i in range(3):
    print(i)
    
x = "5"
y = 2
print(x * y)
# Ejecutar la ventana
ventana.mainloop()