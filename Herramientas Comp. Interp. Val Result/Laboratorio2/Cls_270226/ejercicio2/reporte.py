import webbrowser
from pathlib import Path

print("=== Mini Reporte (HTML + CSS) ===")


def leer_venta(etiqueta):
    try:
        valor = float(input(f"{etiqueta} venta positiva: "))
    except ValueError:
        print("Alguna nota no es un numero. Intente de nuevo")
        raise SystemExit
    if valor < 0:
        print("Las ventas no pueden ser negativas")
        raise SystemExit
    return valor


nombre = input("Nombre del vendedr : ").strip()
v1 = leer_venta("Venta 1")
v2 = leer_venta("Venta 2")
v3 = leer_venta("Venta 3")

totalVentas = v1+v2+v3
totalComision = totalVentas * 0.1
valorFinal = totalVentas + totalComision

if totalVentas >= 5000000:
    estado = "EXCELENTE"
elif totalVentas >= 3000000 and totalVentas < 5000000:
    estado = "BUENO"
else:
    estado = "REGULAR"

if estado == "EXCELENTE" or estado == "BUENO":
    clase_estado = "ok"
else:
    clase_estado = "regular"

base = Path(__file__).parent
ruta_plantilla = base / "plantilla.html"
ruta_salida = base / "reporte.html"

try:
    html = ruta_plantilla.read_text(encoding="utf-8")
except FileNotFoundError:
    print("No se encontro plantilla html. Asegurate de que este en la misma carpeta")
    raise SystemExit

html = (html
        .replace("{{NOMBRE}}", nombre or "—")
        .replace("{{V1}}", f"{v1:.0f}")
        .replace("{{V2}}", f"{v2:.0f}")
        .replace("{{V3}}", f"{v3:.0f}")
        .replace("{{TOTALVENTAS}}", f"{totalVentas:.0f}")
        .replace("{{COMISIONES}}", f"{totalComision:.0f}")
        .replace("{{VALORFINAL}}", f"{valorFinal:.0f}")
        .replace("{{ESTADO}}", estado)
        .replace("{{CLASE_ESTADO}}", clase_estado)
        )

ruta_salida.write_text(html, encoding="utf-8")
print(f"archivo generado: {ruta_salida.name}")

webbrowser.open_new_tab(ruta_salida.as_uri())
