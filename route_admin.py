from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
from flask import session
from sqlalchemy.dialects.postgresql import ARRAY


app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:7d5ef1@127.0.0.1:5432/try'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
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
    carburant = db.relationship('DetailsCarburant', backref='produit')
    gaz = db.relationship('DetailsGaz', backref='produit')
    lub = db.relationship('DetailsLub', backref='produit')
    batterie = db.relationship('DetailsBat', backref='produit')
    pneu = db.relationship('DetailsPneu', backref='produit')
    entretien = db.relationship('DetailsEntre', backref='produit')
    refroidissement = db.relationship('DetailsRefroi', backref='produit')
    detendeur = db.relationship('DetailsDet', backref='produit')
class DetailsCarburant(db.Model):
    __tablename__ = 'carburant'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(db.String(1000))
    avantage = db.Column(db.String(1000), nullable=False)
    additifs = db.Column(db.String(1000), nullable=False)
    normes = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsGaz(db.Model):
    __tablename__ = 'gaz'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete='SET NULL'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utilliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(ARRAY(db.String))
    avantage = db.Column(db.String(1000), nullable=False)
    additifs = db.Column(db.String(1000), nullable=False)
    normes = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsLub(db.Model):
    __tablename__ = 'lubrifiants'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete='SET NULL'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(ARRAY(db.String))
    avantage = db.Column(db.String(1000), nullable=False)
    normes = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsBat(db.Model):
    __tablename__ = 'batteries'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete='SET NULL'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(ARRAY(db.String))
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
    moteurs = db.Column(ARRAY(db.String))
    avantage = db.Column(db.String(1000), nullable=False)
    composant = db.Column(db.String(1000), nullable=False)
    instruction = db.Column(db.String(1000), nullable=False)
    recomendation = db.Column(db.String(1000), nullable=False)

class DetailsRefroi(db.Model):
    __tablename__ = 'refroidissement'
    product_id = db.Column(db.Integer, db.ForeignKey('p23.id', onupdate='CASCADE', ondelete='SET NULL'), primary_key=True)
    type = db.Column(db.String(1000), nullable=False)
    utiliser = db.Column(db.String(1000), nullable=False)
    moteurs = db.Column(ARRAY(db.String))
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

@app.route('/admin/choiser/<table_name>')
def choiserune(table_name):
    tables = [
        "carburant",
        "pneumatique",
        "refroidissement",
        "entretien",
        "gaz",
        "batteries",
        "lubrifiant",
        "detendeur"
    ]

    if table_name in tables:
        return render_template(f'admin/{table_name}.html')
    else:
        return "Page non trouvée", 404
@app.route('/admin/voila')
def quide():
    return render_template('admin/choiser.html')

@app.route('/admin', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '12345':
            session['is_admin'] = True
            return redirect(url_for('afficher_produits',nom_categorie='all'))  
        else:
            error = " Identifiants incorrects"
    return render_template('admin/log.html', error=error)


    
@app.route('/admin/ajouter', methods=['GET', 'POST'])
def ajouter_produit():
    if not session.get('is_admin'):
         return redirect(url_for('login')) 
    message = ""
    if request.method == 'POST':
        form_type = str(request.form.get("form_type"))
        try:
            if form_type == "carburant":
                ids = request.form.getlist('id[]')
                noms = request.form.getlist('nom_produit[]')
                types= request.form.getlist('type[]')
                moteurss = request.form.getlist('moteurs[]')
                avantages= request.form.getlist('avantage[]')
                additifss=request.form.getlist('additifs[]')
                normess=request.form.getlist('normes[]')
                recommandations = request.form.getlist('recommandation[]')
                prixs = request.form.getlist('prix[]')
                photos = request.files.getlist('photo[]')

                for i in range(len(noms)):
                    id = int(ids[i]) if ids[i].strip() else None
                    nom = noms[i]
                    type=types[i]
                    moteurs =moteurss[i]
                    avantage=avantages[i]
                    additifs=additifss[i]
                    normes= normess[i]
                    recommandation=recommandations[i]
                    prix = int(prixs[i]) if prixs[i] else 0
                    photo = photos[i]

                    photo_path = None
                    if photo and photo.filename:
                        filename = secure_filename(photo.filename)
                        photo_path = os.path.join('uploads', filename)
                        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                    produit = Produit(
                        id=id,
                        nom_produit=nom,
                        cat_num =1,
                        prix=prix,
                        photo=photo_path
                    )
                    
                    db.session.add(produit)
                    db.session.flush() 
                    carburant_desc=DetailsCarburant(
                        product_id =produit.id,
                        type =type,
                        moteurs =moteurs,
                        avantage =avantage, 
                        additifs = additifs,
                        normes = normes,
                        recomendation =recommandation

                    )
                    db.session.add(carburant_desc)
                    

            elif  form_type == "gaz":
                ids = request.form.getlist('id[]')
                noms = request.form.getlist('nom_produit[]')
                types= request.form.getlist('type[]')
                utillisers= request.form.getlist('utilliser[]')
                avantages= request.form.getlist('avantage[]')
                additifss=request.form.getlist('additifs[]')
                normess=request.form.getlist('normes[]')
                recommandations = request.form.getlist('recommandation[]')
                prixs = request.form.getlist('prix[]')
                photos = request.files.getlist('photo[]')

                for j in range(len(noms)):
                    id = int(ids[j]) if ids[j].strip() else None
                    nom = noms[j]
                    type=types[j]
                    utilliser=utillisers[j]
                    avantage=avantages[j]
                    additifs=additifss[j]
                    normes= normess[j]
                    recommandation=recommandations[j]
                    prix = int(prixs[j]) if prixs[j] else 0
                    photo = photos[j]

                    photo_path = None
                    if photo and photo.filename:
                        filename = secure_filename(photo.filename)
                        photo_path = os.path.join('uploads', filename)
                        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                    produit = Produit(
                        id=id,
                        nom_produit=nom,
                        cat_num =2,
                        prix=prix,
                        photo=photo_path
                    )
                    
                    db.session.add(produit)
                    db.session.flush() 
                    gaz_desc=DetailsGaz(
                        product_id =produit.id,
                        type =type,
                        utilliser=utilliser,
                        avantage =avantage, 
                        additifs = additifs,
                        normes = normes,
                        recomendation =recommandation,
                        moteurs='{"h"}'

                    )
                    
                    db.session.add(gaz_desc)
            elif form_type == "lubrifiant":
                ids = request.form.getlist('id[]')
                noms = request.form.getlist('nom_produit[]')
                types= request.form.getlist('type[]')
                utilisers= request.form.getlist('utilliser[]')
                avantages= request.form.getlist('avantage[]')
                additifss=request.form.getlist('additifs[]')
                normess=request.form.getlist('normes[]')
                recommandations = request.form.getlist('recommandation[]')
                prixs = request.form.getlist('prix[]')
                photos = request.files.getlist('photo[]')

                for j in range(len(noms)):
                    id = int(ids[j]) if ids[j].strip() else None
                    nom = noms[j]
                    type=types[j]
                    utiliser=utilisers[j]
                    avantage=avantages[j]
                    normes= normess[j]
                    recommandation=recommandations[j]
                    prix = int(prixs[j]) if prixs[j] else 0
                    photo = photos[j]

                    photo_path = None
                    if photo and photo.filename:
                        filename = secure_filename(photo.filename)
                        photo_path = os.path.join('uploads', filename)
                        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                    produit = Produit(
                        id=id,
                        nom_produit=nom,
                        cat_num =3,
                        prix=prix,
                        photo=photo_path
                    )
                    
                    db.session.add(produit)
                    db.session.flush() 
                    lub_desc=DetailsLub(
                        product_id =produit.id,
                        type =type,
                        utiliser=utiliser,
                        avantage =avantage, 
                        normes = normes,
                        recomendation =recommandation,
                        moteurs='{"h"}'

                    )
                    
                    db.session.add(lub_desc)
            elif form_type == "batteries":
                ids = request.form.getlist('id[]')
                noms = request.form.getlist('nom_produit[]')
                types= request.form.getlist('type[]')
                utilisers= request.form.getlist('utilliser[]')
                avantages= request.form.getlist('avantage[]')
                additifss=request.form.getlist('additifs[]')
                normess=request.form.getlist('normes[]')
                recommandations = request.form.getlist('recommandation[]')
                prixs = request.form.getlist('prix[]')
                photos = request.files.getlist('photo[]')

                for j in range(len(noms)):
                    id = int(ids[j]) if ids[j].strip() else None
                    nom = noms[j]
                    type=types[j]
                    utiliser=utilisers[j]
                    avantage=avantages[j]
                    normes= normess[j]
                    recommandation=recommandations[j]
                    prix = int(prixs[j]) if prixs[j] else 0
                    photo = photos[j]

                    photo_path = None
                    if photo and photo.filename:
                        filename = secure_filename(photo.filename)
                        photo_path = os.path.join('uploads', filename)
                        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                    produit = Produit(
                        id=id,
                        nom_produit=nom,
                        cat_num =8,
                        prix=prix,
                        photo=photo_path
                    )
                    
                    db.session.add(produit)
                    db.session.flush() 
                    bat_desc=DetailsBat(
                        product_id =produit.id,
                        type =type,
                        utiliser=utiliser,
                        avantage =avantage, 
                        normes = normes,
                        recomendation =recommandation,
                        moteurs='{"h"}'

                    )
                    
                    db.session.add(bat_desc)
            elif form_type == "detendeur":
                ids = request.form.getlist('id[]')
                noms = request.form.getlist('nom_produit[]')
                types= request.form.getlist('type[]')
                utilisers= request.form.getlist('utiliser[]')
                avantages= request.form.getlist('avantage[]')
                composants=request.form.getlist('composant[]')
                compatibilites=request.form.getlist('compatibilite[]')
                normess=request.form.getlist('norm[]')
                recomendations = request.form.getlist('recomendation[]')
                prixs = request.form.getlist('prix[]')
                photos = request.files.getlist('photo[]')

                for j in range(len(noms)):
                    id = int(ids[j]) if ids[j].strip() else None
                    nom = noms[j]
                    type=types[j]
                    utiliser=utilisers[j]
                    avantage=avantages[j]
                    compatibilite=compatibilites[j]
                    composant=composants[j]
                    norm= normess[j]
                    recomendation=recomendations[j]
                    prix = int(prixs[j]) if prixs[j] else 0
                    photo = photos[j]

                    photo_path = None
                    if photo and photo.filename:
                        filename = secure_filename(photo.filename)
                        photo_path = os.path.join('uploads', filename)
                        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                    produit = Produit(
                        id=id,
                        nom_produit=nom,
                        cat_num =7,
                        prix=prix,
                        photo=photo_path
                    )
                    
                    db.session.add(produit)
                    db.session.flush() 
                    det_desc=DetailsDet(
                        product_id =produit.id,
                        type =type,
                        compatibilite=compatibilite,
                        composant=composant,
                        utiliser=utiliser,
                        avantage =avantage, 
                        norm=norm,
                        recomendation =recomendation,
                        

                    )
                    
                    db.session.add(det_desc)
            elif form_type == "pneumatique":
                ids = request.form.getlist('id[]')
                noms = request.form.getlist('nom_produit[]')
                types= request.form.getlist('type[]')
                utilisers= request.form.getlist('utiliser[]')
                avantages= request.form.getlist('avantage[]')
                dimention=request.form.getlist('dimention[]')
                recomendations = request.form.getlist('recomendation[]')
                prixs = request.form.getlist('prix[]')
                photos = request.files.getlist('photo[]')

                for j in range(len(noms)):
                    id = int(ids[j]) if ids[j].strip() else None
                    nom = noms[j]
                    type=types[j]
                    utiliser=utilisers[j]
                    avantage=avantages[j]
                    dimention=dimention[j]
                    recomendation=recomendations[j]
                    prix = int(prixs[j]) if prixs[j] else 0
                    photo = photos[j]

                    photo_path = None
                    if photo and photo.filename:
                        filename = secure_filename(photo.filename)
                        photo_path = os.path.join('uploads', filename)
                        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                    produit = Produit(
                        id=id,
                        nom_produit=nom,
                        cat_num =4,
                        prix=prix,
                        photo=photo_path
                    )
                    
                    db.session.add(produit)
                    db.session.flush() 
                    pn_desc=DetailsPneu(
                        product_id =produit.id,
                        type =type,
                        utiliser=utiliser,
                        avantage =avantage, 
                        dimention=dimention,
                        recomendation =recomendation,
                        

                    )
                    
                    db.session.add(pn_desc)
               
            elif form_type == "refroidissement":
                ids = request.form.getlist('id[]')
                noms = request.form.getlist('nom_produit[]')
                types= request.form.getlist('type[]')
                utilisers= request.form.getlist('utiliser[]')
                avantages= request.form.getlist('avantage[]')
                composant=request.form.getlist('composant[]')
                normess=request.form.getlist('normes[]')
                recommandations = request.form.getlist('recommandation[]')
                prixs = request.form.getlist('prix[]')
                photos = request.files.getlist('photo[]')

                for j in range(len(noms)):
                    id = int(ids[j]) if ids[j].strip() else None
                    nom = noms[j]
                    type=types[j]
                    utiliser=utilisers[j]
                    composant=composant[j]
                    avantage=avantages[j]
                    normes= normess[j]
                    recommandation=recommandations[j]
                    prix = int(prixs[j]) if prixs[j] else 0
                    photo = photos[j]

                    photo_path = None
                    if photo and photo.filename:
                        filename = secure_filename(photo.filename)
                        photo_path = os.path.join('uploads', filename)
                        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                    produit = Produit(
                        id=id,
                        nom_produit=nom,
                        cat_num =5,
                        prix=prix,
                        photo=photo_path
                    )
                    
                    db.session.add(produit)
                    db.session.flush() 
                    re_desc=DetailsRefroi(
                        product_id =produit.id,
                        type =type,
                        utiliser=utiliser,
                        avantage =avantage, 
                        norm= normes,
                        composant=composant,
                        recomendation =recommandation,
                        moteurs='{"h"}'

                    )
                    
                    db.session.add(re_desc)

            elif form_type == "entretien":
                ids = request.form.getlist('id[]')
                noms = request.form.getlist('nom_produit[]')
                types= request.form.getlist('type[]')
                utilisers= request.form.getlist('utiliser[]')
                avantages= request.form.getlist('avantage[]')
                composant=request.form.getlist('composant[]')
                instruction=request.form.getlist('instruction[]')
                recommandations = request.form.getlist('recommandation[]')
                prixs = request.form.getlist('prix[]')
                photos = request.files.getlist('photo[]')

                for j in range(len(noms)):
                    id = int(ids[j]) if ids[j].strip() else None
                    nom = noms[j]
                    type=types[j]
                    utiliser=utilisers[j]
                    composant=composant[j]
                    avantage=avantages[j]
                    instruction=instruction[j]
                    recommandation=recommandations[j]
                    prix = int(prixs[j]) if prixs[j] else 0
                    photo = photos[j]

                    photo_path = None
                    if photo and photo.filename:
                        filename = secure_filename(photo.filename)
                        photo_path = os.path.join('uploads', filename)
                        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                    produit = Produit(
                        id=id,
                        nom_produit=nom,
                        cat_num =6,
                        prix=prix,
                        photo=photo_path
                    )
                    
                    db.session.add(produit)
                    db.session.flush() 
                    ent_desc=DetailsEntre(
                        product_id =produit.id,
                        type =type,
                        utiliser=utiliser,
                        avantage =avantage, 
                        instruction=instruction,
                        composant=composant,
                        recomendation =recommandation,
                        moteurs='{"h"}'

                    )
                    
                    db.session.add(ent_desc)
            db.session.commit()
            message = "✅ Tous les produits ont été ajoutés avec succès !"
            return redirect(url_for('ajouter_produit'))

        except Exception as e:
            message = f"❌ Erreur : {str(e)}"

    
    return render_template('admin/ajt.html', message=message)


@app.route('/admin/chercher', methods=['GET', 'POST'])
def chercher_produits():
    if not session.get('is_admin'):
         return redirect(url_for('login')) 
    produit = None
    message = ""

    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        if query:
            if query.isdigit():
                produit = Produit.query.filter_by(id=int(query)).first()
            else:
                produit = Produit.query.filter(Produit.nom_produit.ilike(f"%{query}%")).first()

            if not produit:
                message = f"Aucun produit trouvé pour « {query} »."
    
    
    return render_template('admin/search.html', produit=produit, message=message)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_produit(id):
    if not session.get('is_admin'):
         return redirect(url_for('login')) 
    produit = Produit.query.get_or_404(id)
    
    if produit.photo:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], os.path.basename(produit.photo)))
        except:
            pass
    
    db.session.delete(produit)
    db.session.commit()
    return redirect(url_for('suppremer_produit'))

@app.route('/modifier/<int:id>', methods=['GET', 'POST'])
def modifier_produit(id):
    if not session.get('is_admin'):
         return redirect(url_for('login')) 
    produit = Produit.query.get_or_404(id)
    message = ""

    if request.method == 'POST':
        try:
            produit.nom_produit = request.form['nom_produit']
         #   produit.categorie = request.form['categorie']
            produit.prix = int(request.form['prix']) 
           # produit.description = request.form['description']
            
            photo = request.files['photo']
            if photo and photo.filename: 
                # Supprimer l'ancienne photo si existante
                if produit.photo:
                    try:
                        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], os.path.basename(produit.photo)))
                    except:
                        pass

                filename = secure_filename(photo.filename)
                photo_path = os.path.join('uploads', filename)
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                produit.photo = photo_path

            db.session.commit()
            message = "Produit modifié avec succès !"
            return redirect(url_for('changer_details'))
        except ValueError:
            message = "Erreur : Le prix et la quantité doivent être des nombres valides"
        except Exception as e:
            message = f"Erreur : {str(e)}"

    
    produits = Produit.query.all()

    return render_template('admin/changer.html', produits=produits, produit=produit, message=message)

@app.route('/admin/changer')
def changer_details():
    if not session.get('is_admin'):
         return redirect(url_for('login')) 
    produits = Produit.query.all()
    return render_template('admin/changer.html', produits=produits,produit=None)

@app.route('/admin/supremer')
def suppremer_produit():
   if not session.get('is_admin'):
         return redirect(url_for('login')) 
   produits = Produit.query.all()
   return render_template('admin/dellet_page.html', produits=produits)

@app.route('/admin/affiche/<nom_categorie>')
def afficher_produits(nom_categorie):
    if not session.get('is_admin'):
        return redirect(url_for('login')) 
    if nom_categorie=='all':
      produits = Produit.query.all()
    else:  
     produits = Produit.query.filter_by( cat_num=nom_categorie).all()
    return render_template('admin/voir.html', produits=produits)

@app.route('/admin/logout')
def logout():
    if not session.get('is_admin'):
         return redirect(url_for('login')) 
    session.pop('is_admin', None)
    return redirect(url_for('login'))


