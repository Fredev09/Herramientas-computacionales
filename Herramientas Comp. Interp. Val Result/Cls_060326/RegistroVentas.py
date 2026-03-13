import webbrowser
from pathlib import Path

# Programa para registrar vendedor y cantidad de ventas con while
# solicitar al usuario la cantidad de vendedores a registrar
try:
    N = int(input("Solicitar que ingrese la cantidad de vendedores: "))
except ValueError:
    print("Tiene q ser un numero entero")
    raise SystemExit

# crear una lista vacia para guardar la inf de los vendedores
vendedores = []

# contador para recorrer a los vendedores
i = 1

# ciclo while que se ejecute hasta que i sea igual al num de vendedores
while i <= N:
    # mostrar en pantalla que vendedor se esta registrando
    print("\nRegistro del vendedor", i)

    # solicitar el nombre del vendedor
    nombre = input("VENDEDOR {}: ".format(i))

    # solicitar la cantidad de ventas que realizo el vendedor
    try:
        M = int(input("Solicitar que ingrese la cantidad de ventas : "))
    except ValueError:
        print("Error la cantidad de ventas debe ser un numero")
        raise SystemExit

    # crear una lista vacia para guardar la inf de las ventas
    ventas = []

    # contador para recorrer las ventas
    j = 1

    # while para ingresar la inf de las ventas
    while j <= M:
        # solicitar el nombre de la venta
        nombreProducto = input("VENTA {}: ".format(j))

        try:
            precioProducto = float(input("PRECIO DE LA VENTA {}: ".format(j)))
            cantidadProducto = int(input("CANTIDAD DE LA VENTA {}: ".format(j)))
        except ValueError:
            print("Error el precio y la cantidad deben ser numeros")
            raise SystemExit

        #calculamos cosas matematicas
        totalVentas = precioProducto * cantidadProducto

        # agregar el nombre de la venta a la lista de ventas
        ventas.append({
            "nombre": nombreProducto,
            "precio": precioProducto,
            "cantidad": cantidadProducto,
            "totalVentas": totalVentas
        })

        # incrementar el contador de ventas
        j += 1

    # crear un diccionario con la informacion del vendedor
    vendedor = {
        "nombre": nombre,
        "ventas": ventas
    }

    # agregamos el diccionario del vendedor a la lista de vendedores
    vendedores.append(vendedor)

    # incrementar el contador de vendedores
    i += 1


base = Path(__file__).parent
ruta_plantilla = base / "plantilla.html"
ruta_salida = base / "reporte_ventas.html"

try:
    html = ruta_plantilla.read_text(encoding="utf-8")
except FileNotFoundError:
    print("No se encontro plantilla html. Asegurate de que este en la misma carpeta")
    raise SystemExit


# plantilla para cada vendedor para ir almacenandolos eb cartas
plantilla_vendedor = """
<div class="card">
    <p><strong>Vendedor:</strong> {{NOMBRE}}</p>

    <ul>
        {{VENTAS}}
    </ul>
</div>
"""

# variable para guardar todos los vendedores en html
body_vendedores = ""

# reiniciar el contador para recorrer los vendedores registrados
i = 0

# ciclo para recorrer los vendedores registrados
while i < len(vendedores):

    # reiniciar la lista de ventas para el nuevo vendedor
    plantilla_lista_ventas = ""

    # reiniciar contador para recorrer las ventas
    j = 0

    # ciclo while para recorrer la lista de ventas
    while j < len(vendedores[i]["ventas"]):
        venta = vendedores[i]["ventas"][j]

        plantilla_lista_ventas += f"""<li>
        Producto: {venta['nombre']} <br>
        Precio: {venta['precio']} <br>
        Cantidad: {venta['cantidad']} <br>
        Total: {venta['totalVentas']} 
        </li>"""
        j += 1

    # rellenar la plantilla del vendedor actual
    carta_vendedor = (plantilla_vendedor
                      .replace("{{NOMBRE}}", vendedores[i]["nombre"])
                      .replace("{{VENTAS}}", plantilla_lista_ventas)
                      )

    # guardar ese bloque en el contenido general
    body_vendedores += carta_vendedor

    # incrementar el contador de vendedores
    i += 1

# reemplazar en la plantilla principal
html = html.replace("{{VENDEDORES}}", body_vendedores)

ruta_salida.write_text(html, encoding="utf-8")
print(f"archivo generado: {ruta_salida.name}")

webbrowser.open_new_tab(ruta_salida.as_uri())
