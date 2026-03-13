def mediaYmediana():
    suma = 0
    notas = []
   
    while True:
        
        info = input("Ingrese la nota o 'fin': ")
    
        try:
            info = float(info)
            notas.append(info)
            suma+=info
        except ValueError:
            if info.lower() == 'fin':
               break
            else:
               print("Entrada no valida")

    cant = len(notas)

    if cant != 0:
      notas.sort()
      promedio = suma / cant

      if cant % 2 == 0:
         mediana = (notas[cant // 2 - 1] + notas[cant // 2]) / 2
      else:
         mediana = notas[cant // 2]
    else:
       print("No se ha ingresado ninguna nota")
       return

    print(f"El promedio es: {promedio:.2f} \nLa mediana es: {mediana:.2f}")
   
mediaYmediana()
