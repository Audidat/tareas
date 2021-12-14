from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

tareasInicial = ['Hacer la compra','Echar gasolina']

@app.route("/")
def tareas():
    return render_template("lista.html", tareas=tareasInicial)

@app.route("/add")
def add():
    tarea = request.args.get('tarea')
    tareasInicial.append(tarea)
    return redirect(url_for('tareas'))

@app.route("/delete/<int:tarea_id>")
def delete(tarea_id):
    del tareasInicial[tarea_id]
    return redirect(url_for('tareas'))
