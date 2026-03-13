def registro_usuario():

    total = 0
    mayores = 0

    while True:
        nombre = input("Ingrese nombre o 'salir': ")
        if nombre.lower() == 'salir':
            break
        edad = int(input("Ingrese edad: "))
        total += 1
        if edad >= 18:
            mayores += 1
    print(f"Total de registrados: {total}")
    print(f"Mayores de edad: {mayores}")


registro_usuario()
