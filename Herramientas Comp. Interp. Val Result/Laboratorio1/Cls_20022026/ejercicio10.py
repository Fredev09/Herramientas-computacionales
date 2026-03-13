def generadorCarnets():

    cont = 1

    while True:

        nombre = input("Ingrese un nombre o 'fin': ")
        inicialesNombre = ""

        if nombre.lower() == 'fin':
            print("Fin del programa")
            break
        else:
            nombres = nombre.split()
            for iniciales in nombres:
                inicialesNombre += iniciales[0].upper() 

        carnet = f"{inicialesNombre}{cont:08d}"

        print(f"Carnet para el estudiante: {nombre} se ha generado correctamente el codigo es: {carnet}")

        cont+=1

generadorCarnets()
