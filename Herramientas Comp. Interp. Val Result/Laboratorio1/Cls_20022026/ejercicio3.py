def calculadora():

    try:
        num = int(input("Ingrese el numero a multiplicar"))
    except ValueError:
        print("Debe ingresar un numero entero")
        return
    
    for i in range(11):
            print(f"{num} * {i} = {num*i}")

calculadora()