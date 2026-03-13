import webbrowser
from pathlib import Path

print("=== Mini Reporte (HTML + CSS) ===")


def leer_nota(etiqueta):
    try:
        valor = float(input(f"{etiqueta} (0.0 a 5.0): "))
    except ValueError:
        print("Alguna nota no es un numero. Intente de nuevo")
        raise SystemExit
    if valor < 0 or valor > 5:
        print("Las notas deben estar entre 0.0 y 5.0")
        raise SystemExit
    return valor


nombre = input("Nombre del estudiante: ").strip()
n1 = leer_nota("Parcial")
n2 = leer_nota("Talleres")
n3 = leer_nota("Proyecto final")

promedio = (n1*0.3 + n2*0.3 + n3*0.4)

if promedio >= 4.5:
    estado = "superior"
elif promedio >= 4.0 and promedio < 4.5:
    estado = "alto"
elif promedio >= 3.0 and promedio < 4.0:
    estado = "basico"
else:
    estado = "bajo"

if estado == "superior" or estado == "alto":
    clase_estado = "ok"
elif estado == "basico":
    clase_estado = "regular"
else:
    clase_estado = "bad"

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
        .replace("{{N1}}", f"{n1:.2f}")
        .replace("{{N2}}", f"{n2:.2f}")
        .replace("{{N3}}", f"{n3:.2f}")
        .replace("{{PROMEDIO}}", f"{promedio:.2f}")
        .replace("{{ESTADO}}", estado)
        .replace("{{CLASE_ESTADO}}", clase_estado)
        )

ruta_salida.write_text(html, encoding="utf-8")
print(f"archivo generado: {ruta_salida.name}")

webbrowser.open_new_tab(ruta_salida.as_uri())
