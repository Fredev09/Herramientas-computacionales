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
n1 = leer_nota("Nota 1")
n2 = leer_nota("Nota 2")
n3 = leer_nota("Nota 3")

promedio = (n1 + n2 + n3) / 3

estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
clase_estado = "ok" if estado == "APROBADO" else "bad"

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