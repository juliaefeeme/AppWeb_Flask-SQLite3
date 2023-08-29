from flask import Flask, render_template, request, redirect, url_for

#Dar acceso a los demás ficheros
import db
from models import Tarea

#inicializar servidor con app
app=Flask(__name__)

@app.route("/")
def home():
    todas_las_tareas=db.session.query(Tarea).all()
    return render_template("index.html", lista_de_tareas=todas_las_tareas) #render_template para cargar de cero la web

@app.route("/crear-tarea", methods=["POST"])
def crear():
    tarea=Tarea(contenido=request.form['contenido-tarea'], hecha=False)
    db.session.add(tarea) #Añadir el objeto a la base de datos
    db.session.commit() #Ejecutar la operación pendiente de la base de datos
    db.session.close()
    return redirect(url_for("home"))

@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    tarea=db.session.query(Tarea).filter_by(id=id).delete()
    db.session.commit() #Ejecutar la operación pendiente de la base de datos
    db.session.close()
    return redirect(url_for("home"))

@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea=db.session.query(Tarea).filter_by(id=id).first()
    tarea.hecha=not(tarea.hecha)
    db.session.commit() #Ejecutar la operación pendiente de la base de datos
    db.session.close()
    return redirect(url_for("home"))

if __name__=="__main__":
    db.Base.metadata.create_all(db.engine) #Creamos el modelo de datos
    app.run(debug=True)