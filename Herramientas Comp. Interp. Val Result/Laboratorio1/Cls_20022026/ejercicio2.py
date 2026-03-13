def calcular_matricula():

    numCreditos =  int(input("Ingrese el numero de creditos: "))
    valorCredito = float(input(f"Ingrese el valor del credito: "))
    promedio = float(input(f"Ingrese el promedio: "))
    valorMatricula = valorCredito * numCreditos


    if numCreditos > 18 and promedio > 4.5:
            descuento = valorMatricula * 0.10
            valorMatricula -= descuento
            print("usted recibe un descuento de 10%")

    elif numCreditos < 12 and promedio < 3.5:
            recargo = valorMatricula * 0.05
            valorMatricula += recargo
            print("usted recibe un recargo de 5%")
    else:
           print("Usted no recibe ni descuento ni recargo")

    print(f"El valor de su matricula queda en: {valorMatricula:.2f}")

calcular_matricula()