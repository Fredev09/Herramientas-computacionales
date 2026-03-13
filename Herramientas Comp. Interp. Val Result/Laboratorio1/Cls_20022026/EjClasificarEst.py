def clasificar_estudiante(promedio):
    """
    Clasifica a un estudiante segun su promedio.
    
    Parametros:
    promedio (float): nota promedio del estudiante.
    
    Retorna:
    str: Clasificacion del estudiante segun su rendimiento.
    """
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Regular"
    else:
        return "Reprobado"

# Prueba con un valor ingresado por el usuario
promedio = float(input("Ingrese el promedio del estudiante: "))
print("Clasificacion:", clasificar_estudiante(promedio))