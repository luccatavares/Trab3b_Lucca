from database import db

class Editoras(db.Model):
    __tablename__ = 'editora'
    id_editora = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(50))
   
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade
    
    def __repr__(self):
        return f"<Editora {self.nome}>"
    

class Autores(db.Model):
    __tablename__ = 'autore'
    id_autor = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    id_editora = db.Column(db.Integer, db.ForeignKey('editoras.id_editora'))

    editora = db.relationship('Editora', foreign_keys=id_editora)

    def __init__(self, nome, email, id_editora):
        self.nome = nome
        self.email = email
        self.id_editora = id_editora
    
    def __repr__(self):
        return f"<Cadastro: {self.nome} - {self.email} - {self.id_editora}> "