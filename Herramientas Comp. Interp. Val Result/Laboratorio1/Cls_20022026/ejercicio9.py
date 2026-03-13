def notasEst():

    listaEstudiantes = []

    while True:
        op = input("Desea ingresar un estudiante? 's/n': ")

        if op.lower() == 's':
            nombre = input("Ingrese el nombre del estudiante: ")
            promedio = float(input("Ingrese el promedio del estudiante: "))

            listaEstudiantes.append({
            "Nombre": nombre,
            "Promedio": promedio
        })

        elif op.lower() == 'n':
            print("Finalizando....")
            break
        else:
            print("Ingrese una opcion valida")

    cant = len(listaEstudiantes)

    if cant == 0:
        print("No se registraron estudiantes")
    else:

        print("Estos son los 3 estudiantes con mejor rendimiento: ")
        listaEstudiantes.sort(key=lambda nota: nota["Promedio"], reverse=True)

        tresMejores = listaEstudiantes[:3]

        for i in tresMejores:
            print(f"Nombre: {i['Nombre']} - Promedio: {i['Promedio']}")

notasEst()