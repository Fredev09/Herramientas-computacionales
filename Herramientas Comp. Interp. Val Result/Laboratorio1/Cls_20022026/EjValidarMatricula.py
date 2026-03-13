# Definimos una funcion llamada validar_matricula con tres parametros de entrada
def validar_matricula(asignaturas_aprobadas, total_asignaturas, tiene_deuda):
    """
    Valida si un estudiante puede matricularse segun sus asignaturas aprobadas y si tiene deuda
    """

    # Calculamos el porcentaje de asignaturas aprobadas
    porcentaje_aprobado = (asignaturas_aprobadas / total_asignaturas) * 100

    # Evaluamos si el estudiante aprobo al menos el 60% y no tiene deudas
    if porcentaje_aprobado >= 60 and not tiene_deuda:
        return "Matricula permitida"  # Si cumple ambas condiciones, se permite la matricula
    else:
        return "Matricula denegada"  # Si no cumple alguna condicion, se deniega la matricula


# --------------------------
# Bloque de entrada de datos
# --------------------------

# Solicitamos al usuario ingresar cuantas asignaturas aprobo
aprobadas = int(input("Asignaturas aprobadas: "))

# Solicitamos el total de asignaturas cursadas el semestre anterior
total = int(input("Total de asignaturas del semestre anterior: "))

# Preguntamos si tiene deuda. Si responde "s", se interpreta como True
deuda = input("Tiene deuda? (s/n): ").strip().lower() == "s"

# Llamamos a la funcion con los datos ingresados y mostramos el resultado
print(validar_matricula(aprobadas, total, deuda))