from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Categorie(db.Model):
    __tablename__ = 'categorie'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    
    produits = db.relationship('Produit', backref='categorie', lazy=True)


class Produit(db.Model):
    __tablename__ = 'p23'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nom_produit = db.Column(db.String(100), nullable=False)
    prix = db.Column(db.Integer, nullable=False)
    cat_num = db.Column(db.Integer, db.ForeignKey('categorie.id', onupdate='CASCADE', ondelete='SET NULL'), nullable=True)
    photo = db.Column(db.String(200), nullable=True)

    #relationship (ORM)
    carburant = db.relationship('DetailsCarburant', backref='produit', uselist=False)
    gaz = db.relationship('DetailsGaz', backref='produit', uselist=False)
    lub = db.relationship('DetailsLub', backref='produit', uselist=False)
    batterie = db.relationship('DetailsBat', backref='produit', uselist=False)
    pneu = db.relationship('DetailsPneu', backref='produit', uselist=False)
    entretien = db.relationship('DetailsEntre', backref='produit', uselist=False)
    refroidissement = db.relationship('DetailsRefroi', backref='produit', uselist=False)
    detendeur = db.relationship('DetailsDet', backref='produit', uselist=False)
class DetailsCarburant(db.Model):
    __tablename__ = 'carburant'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete='SET NULL'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    indice_octane = db.Column(db.Integer, nullable=False)
    moteurs = db.Column(db.String(1000), nullable=False)
    avantage = db.Column(db.String(1000), nullable=False)
    additifs = db.Column(db.String(1000), nullable=False)
    normes = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsGaz(db.Model):
    __tablename__ = 'gaz'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete='SET NULL'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(db.String(1000), nullable=False)
    avantage = db.Column(db.String(1000), nullable=False)
    additifs = db.Column(db.String(1000), nullable=False)
    normes = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsLub(db.Model):
    __tablename__ = 'lubrifiants'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete='SET NULL'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(db.String(1000), nullable=False)
    avantage = db.Column(db.String(1000), nullable=False)
    normes = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsBat(db.Model):
    __tablename__ = 'batteries'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete='SET NULL'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(db.String(1000), nullable=False)
    avantage = db.Column(db.String(1000), nullable=False)
    normes = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsPneu(db.Model):
    __tablename__ = 'pneu'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete='SET NULL'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    avantage = db.Column(db.String(1000), nullable=False)
    dimention = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsEntre(db.Model):
    __tablename__ = 'entretien'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete='SET NULL'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(db.String(1000), nullable=False)
    avantage = db.Column(db.String(1000), nullable=False)
    composant = db.Column(db.String(1000), nullable=False)
    instruction = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsRefroi(db.Model):
    __tablename__ = 'refroidissement'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete='SET NULL'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(db.String(1000), nullable=False)
    avantage = db.Column(db.String(1000), nullable=False)
    composant = db.Column(db.String(1000), nullable=False)
    norm = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsDet(db.Model):
    __tablename__ = 'detendeur'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete='SET NULL'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    compatibilite = db.Column(db.String(1000), nullable=False)
    avantage = db.Column(db.String(1000), nullable=False)
    composant = db.Column(db.String(1000), nullable=False)
    norm = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)



