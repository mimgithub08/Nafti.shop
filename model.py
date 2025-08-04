from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produit(db.Model):
    __tablename__ = 'p23'
    id = db.Column(db.Integer, primary_key=True)
    nom_produit = db.Column(db.String(100), nullable=False)
    categorie = db.Column(db.String(50), nullable=False)
    prix = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    photo = db.Column(db.String(200), nullable=True)
