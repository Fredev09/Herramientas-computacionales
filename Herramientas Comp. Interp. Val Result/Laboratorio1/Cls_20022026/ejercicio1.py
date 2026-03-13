def calculo_promedio():
    cant = int(input("Ingrese la cantidad de notas"))
    suma = 0

    for i in range(cant):
        nota = float(input(f"Ingrese nota {i+1}: "))
        suma += nota

    promedio = suma/cant
    print(f"el promedio final es{promedio:.2f}")
 
    if promedio >= 3.0:
       print("Usted ha aprobado")
    elif promedio <= 2.0:
       print("usted refuerzo")
    else:
       print("usted pierde")

calculo_promedio()
