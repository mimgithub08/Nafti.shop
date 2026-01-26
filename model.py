from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY
db = SQLAlchemy()
class Categorie(db.Model):
    __tablename__ = 'categorie'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    produits = db.relationship('Produit', backref='categorie', lazy=True)


class Produit(db.Model):
    __tablename__ = 'p23'
    id = db.Column(db.Integer, primary_key=True)
    nom_produit = db.Column(db.String(100), nullable=False)
    prix = db.Column(db.Integer, nullable=False)
    cat_num = db.Column(db.Integer, db.ForeignKey('categorie.id', onupdate='CASCADE'), nullable=True)
    photo = db.Column(db.String(200), nullable=True)

    #relationship (ORM)
    carburant = db.relationship('DetailsCarburant', backref='produit',  cascade="all, delete",
    passive_deletes=True)
    gaz = db.relationship('DetailsGaz', backref='produit',  cascade="all, delete",
    passive_deletes=True)
    lub = db.relationship('DetailsLub', backref='produit',  cascade="all, delete",
    passive_deletes=True)
    batterie = db.relationship('DetailsBat', backref='produit',  cascade="all, delete",
    passive_deletes=True)
    pneu = db.relationship('DetailsPneu', backref='produit',  cascade="all, delete",
    passive_deletes=True)
    entretien = db.relationship('DetailsEntre', backref='produit',  cascade="all, delete",
    passive_deletes=True)
    refroidissement = db.relationship('DetailsRefroi', backref='produit',  cascade="all, delete",
    passive_deletes=True)
    detendeur = db.relationship('DetailsDet', backref='produit',  cascade="all, delete",
    passive_deletes=True)
class DetailsCarburant(db.Model):
    __tablename__ = 'carburant'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete="CASCADE"), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(db.String(1000))
    avantage = db.Column(db.String(1000), nullable=False)
    additifs = db.Column(db.String(1000), nullable=False)
    normes = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsGaz(db.Model):
    __tablename__ = 'gaz'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete="CASCADE"), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utilliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(db.String(100))
    avantage = db.Column(db.String(1000), nullable=False)
    additifs = db.Column(db.String(1000), nullable=False)
    normes = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsLub(db.Model):
    __tablename__ = 'lubrifiants'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete="CASCADE"), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(db.String(100))
    avantage = db.Column(db.String(1000), nullable=False)
    normes = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsBat(db.Model):
    __tablename__ = 'batteries'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete="CASCADE"), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(db.String(100))
    avantage = db.Column(db.String(1000), nullable=False)
    normes = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsPneu(db.Model):
    __tablename__ = 'pneu'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete="CASCADE"), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    avantage = db.Column(db.String(1000), nullable=False)
    dimention = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsEntre(db.Model):
    __tablename__ = 'entretien'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete="CASCADE"), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(db.String(100))
    avantage = db.Column(db.String(1000), nullable=False)
    composant = db.Column(db.String(1000), nullable=False)
    instruction = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsRefroi(db.Model):
    __tablename__ = 'refroidissement'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete="CASCADE"), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(db.String(100))
    avantage = db.Column(db.String(1000), nullable=False)
    composant = db.Column(db.String(1000), nullable=False)
    norm = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsDet(db.Model):
    __tablename__ = 'detendeur'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    compatibilite = db.Column(db.String(1000), nullable=False)
    avantage = db.Column(db.String(1000), nullable=False)
    composant = db.Column(db.String(1000), nullable=False)
    norm = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)
