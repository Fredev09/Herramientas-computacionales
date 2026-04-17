from flask import Flask, render_template, request, redirect, url_for, flash
import estudiantes

app = Flask(__name__)

estudiante = estudiantes.Estudiantes()
app.secret_key = "clave"

@app.route("/")
def inicio():
    resultado = estudiante.listar()
    return render_template("index.html", listado=resultado)


@app.route("/guardar", methods=["POST"])
def guardar():
    nombre = request.form["nombre"]
    edad = request.form["edad"]

    estudiante.guardar((nombre, edad))

    flash("Estudiante guardado exitosamente")
    return redirect(url_for("inicio"))


@app.route("/listar")
def listar():
    resultado = estudiante.listar()
    return render_template("index.html", listado=resultado)


@app.route("/consultar", methods=["POST"])
def consultar():
    id = request.form["id"]
    resultado = estudiante.consulta((id,))

    if resultado:
        return render_template("index.html", listado=[resultado])
    else:
        flash("No se encontró el estudiante")
        return redirect(url_for("inicio"))


@app.route("/editar/<int:id>")
def editar(id):
    resultado = estudiante.consulta((id,))
    return render_template("editar.html", dato=resultado)


@app.route("/actualizar", methods=["POST"])
def actualizar():
    id = request.form["id"]
    nombre = request.form["nombre"]
    edad = request.form["edad"]

    estudiante.actualizar((nombre, edad, id))

    flash("Estudiante actualizado exitosamente")
    return redirect(url_for("inicio"))


@app.route("/eliminar/<id>", methods=["POST"])
def eliminar(id):
    estudiante.eliminar((id,))
    flash("Eliminado")
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)
