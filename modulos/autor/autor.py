from flask import Blueprint, render_template, request, redirect, flash
from models import Autores, Editoras
from database import db

bp_autores = Blueprint('autores', __name__, template_folder="templates")

@bp_autores.route("/")
def index():
    a = Autores.query.all()
    return render_template("autores.html", autores=a)


@bp_autores.route("/add")
def add():
    e = Editoras.query.all()
    return render_template("autores_add.html", editoras=e)


@bp_autores.route("/save", methods=['POST'])
def save():
    nome = request.form.get("nome")
    email = request.form.get("email")
    id_autor = request.form.get("id_autor")

    if nome and tipo and id_aluno:
        db_autor = Autores(nome, email, id_autor)
        db.session.add(db_autor)
        db.session.commit()
        flash("Autor salvo!")
        return redirect("/autores")
    else:
        flash("Preencha todos os campos!")
        return redirect("/autores/add")


@bp_autores.route("/remove/<int:id>")
def remove(id):
    a = Autores.query.get(id)
    try:
        db.session.delete(c)
        db.session.commit()
        flash("Autor removido!")
    except:
        flash("Autor inválido!")
    return redirect("/autores")


@bp_autores.route("/edit/<int:id>")
def edit(id):
    a = Autores.query.get(id)
    e = Editoras.query.all()
    return render_template("autor_editar.html", autores=a, editoras=e)


@bp_autores.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    email = request.form.get("email")
    id_editora = request.form.get("id_editora")
    id_autor = request.form.get("id_autor")
    
    if nome and tipo and id_autor and id_editora:
        a = Autores.query.get(id_autor)
        a.nome = nome
        a.email = email
        a.id_autor = id_autor
        db.session.commit()
        flash("Autor editado!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/autor")