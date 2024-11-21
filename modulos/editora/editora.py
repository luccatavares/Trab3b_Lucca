from flask import Blueprint, render_template, request, redirect, flash
from models import Editoras
from database import db

bp_editoras = Blueprint('editora', __name__, template_folder="templates")

@bp_editoras.route("/")
def index():
    e = Editoras.query.all()
    return render_template("editora.html", editora=e)


@bp_editoras.route("/add")
def add():
    return render_template("editora_add.html")


@bp_editoras.route("/save", methods=['POST'])
def save():
    nome = request.form.get("nome")
    cidade = request.form.get("cidade")

    if nome and matricula:
        db_editora = Editoras(nome, cidade)
        db.session.add(db_editora)
        db.session.commit()
        flash("Editora salva!")
        return redirect("/editora")
    else:
        flash("Preencha tudo!")
        return redirect("/editora/add")


@bp_editoras.route("/remove/<int:id>")
def remove(id):
    a = Editoras.query.get(id)
    try:
        db.session.delete(a)
        db.session.commit()
        flash("Editora removido!")
    except:
        flash("Editora inválida!")
    return redirect("/editora")


@bp_editoras.route("/edit/<int:id>")
def edit(id):
    a = Editoras.query.get(id)
    return render_template("editora_editar.html", editora=a)


@bp_editoras.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    cidade = request.form.get("cidade")
    id_aluno = request.form.get("id_editora")
    
    if nome and cidade and id_editora:
        a = Editoras.query.get(id_editora)
        a.nome = nome
        a.cidade = cidade
        db.session.commit()
        flash("Editora editado!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/editora")