def Inasistencia():

    numClases = int(input("Ingrese el numero total de clases: "))
    numInasistencias = int(input("Ingrese el numero de inasistencias: "))

    if numClases==0:
        print("No ha tenido clases")
        return
    
    diferencia = numClases - numInasistencias
    porcentajeAsistencia = (diferencia / numClases) * 100

    print(f"Su porcentaje de asistencia es: {porcentajeAsistencia:.2f} ")

    if porcentajeAsistencia < 75: 
        print("no puede presentar el examen")
    else:
        print("puedes presentar el examen")

Inasistencia()
