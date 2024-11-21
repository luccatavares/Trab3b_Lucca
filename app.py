from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'senha'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/3bim_g1"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
from models import Editoras, Autores
db.init_app(app)
migrate = Migrate(app, db)

from modulos.editora.editora import bp_editoras
app.register_blueprint(bp_editoras, url_prefix='/editora')
from modulos.autor.autor import bp_autores
app.register_blueprint(bp_autores, url_prefix='/autor')

@app.route("/")
def index():
    return render_template("ola.html")