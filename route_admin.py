from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
from flask import session


app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:7d5ef1@127.0.0.1:5432/try'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
db = SQLAlchemy(app)
class Produit(db.Model):
    __tablename__ = 'p23'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nom_produit = db.Column(db.String(100), nullable=False)
    categorie = db.Column(db.String(50), nullable=False)
    prix = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Integer,db.ForeignKey('carburant.desc_id'),nullable=True) 
    photo = db.Column(db.String(200), nullable=True)


class details_carburant(db.Model):
    __tablename__ = 'carburant'
    desc_id=db.Column(db.Integer, primary_key=True, autoincrement=False)
    indice_octane=db.Column(db.Integer, nullable=False)
    moteurs=db.Column(db.String(1000), nullable=False)
    avantage=db.Column(db.String(1000),nullable=False)
    additifs=db.Column(db.String(1000),nullable=False)
    normes=db.Column(db.String(1000),nullable=False)
    recomendation=db.Column(db.String(1000),nullable=False)
 

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
        try:
            ids = request.form.getlist('id[]')
            noms = request.form.getlist('nom_produit[]')
            categories = request.form.getlist('categorie[]')
            prixs = request.form.getlist('prix[]')
            descs = request.form.getlist('description[]')
            photos = request.files.getlist('photo[]')

            for i in range(len(noms)):
                id = int(ids[i]) if ids[i].strip() else None
                nom = noms[i]
                categorie = categories[i]
                prix = int(prixs[i]) if prixs[i] else 0
                desc = descs[i]
                photo = photos[i]

                photo_path = None
                if photo and photo.filename:
                    filename = secure_filename(photo.filename)
                    photo_path = os.path.join('uploads', filename)
                    photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                produit = Produit(
                    id=id,
                    nom_produit=nom,
                    categorie=categorie,
                    prix=prix,
                    description=desc,
                    photo=photo_path
                )
                db.session.add(produit)

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
            produit.categorie = request.form['categorie']
            produit.prix = int(request.form['prix']) 
            produit.description = request.form['description']
            
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
     produits = Produit.query.filter_by(categorie=nom_categorie).all()
    return render_template('admin/voir.html', produits=produits)

@app.route('/admin/logout')
def logout():
    if not session.get('is_admin'):
         return redirect(url_for('login')) 
    session.pop('is_admin', None)
    return redirect(url_for('login'))


