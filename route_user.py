from flask import Flask, render_template,request
import os
from sqlalchemy import func, and_
from sqlalchemy import or_
from sqlalchemy.sql.expression import func
from model import db, Produit, Categorie, DetailsCarburant, DetailsGaz, DetailsLub, DetailsBat, DetailsPneu, DetailsEntre, DetailsRefroi, DetailsDet
from search import search_pro
def init_routes(app):
    @app.route('/chercher', methods=['GET', 'POST'])
    def chercher_du_produits():
        # Récupérer la query depuis le formulaire
        query = request.form.get('query', '').strip()
        
        # Appeler la fonction de recherche
        produits, message, query = search_pro(query)
        
        # Préparer les colonnes pour l'affichage (ajustez selon votre besoin)
        cols = ['nom_produit', 'categorie', 'prix']  # Ajoutez les colonnes que vous voulez afficher
        
        # Afficher le template avec les résultats
        return render_template('user/result.html', 
                            produits=produits, 
                            message=message, 
                            query=query,
                            cols=cols)
    @app.route('/')
    def homepage():

        produits = Produit.query.order_by(func.random()).limit(18).all()
        CONFIG = {
            'carburant': {
                'rel': 'carburant',
                'cols': ['type', 'moteurs', 'avantage', 'additifs', 'normes', 'recomendation']
            },
            'gaz': {
                'rel': 'gaz',
                'cols': ['type', 'utiliser', 'avantage', 'additifs', 'normes', 'recomendation']
            },
            'lub': {
                'rel': 'lub',
                'cols': ['type', 'utiliser', 'moteurs', 'avantage', 'normes', 'recomendation']
            },
            'batterie': {
                'rel': 'batterie',
                'cols': ['type', 'utiliser', 'moteurs', 'avantage', 'normes', 'recomendation']
            },
            'pneu': {
                'rel': 'pneu',
                'cols': ['type', 'utiliser', 'dimention', 'avantage', 'recomendation']
            },
            'entretien': {
                'rel': 'entretien',
                'cols': ['type', 'utiliser', 'composant', 'avantage', 'instruction', 'recomendation']
            },
            'refroidissement': {
                'rel': 'refroidissement',
                'cols': ['type', 'utiliser', 'moteurs', 'composant', 'norm', 'recomendation']
            },
            'detendeur': {
                'rel': 'detendeur',
                'cols': ['type', 'utiliser', 'compatibilite', 'avantage', 'norm', 'recomendation']
            }
        }

        produits_data = []

        for produit in produits:

            row = {
                'id': produit.id,
                'nom': produit.nom_produit,
                'prix': produit.prix,
                'photo': produit.photo,
                'cols': [],
            }

           
            for conf in CONFIG.values():
                details = getattr(produit, conf['rel'])
                if details:
                    d = details[0]
                    row['cols'] = conf['cols']
                    for col in conf['cols']:
                        row[col] = getattr(d, col, '')
                    break

            produits_data.append(row)

        photos = ['slider.png','sliderindex.png']

        return render_template(
            'user/index.html',
            produits=produits_data,
            cols=conf['cols'],
            photos=photos
        )

    
    @app.route('/footer/<nom_page>')
    def page_of_footer(nom_page):
        pages_valides = ['faq', 'contact', 'apropos']
        if nom_page in pages_valides:
            return render_template(f'user/{nom_page}.html')
        else:
            return "Page non trouvée", 404

    @app.route('/produit')
    def page_of_produit():
     return render_template(f'user/produit.html')

    @app.route('/categorie/<nom_categorie>')
    def produit_cat(nom_categorie):

        produits = Produit.query.all()
        messege = "Aucun produit dans cette catégorie"

        CONFIG = {
            'carburant': {
                'rel': 'carburant',
                'cols': ['type', 'moteurs', 'avantage', 'additifs', 'normes', 'recomendation']
            },
            'gaz': {
                'rel': 'gaz',
                'cols': ['type', 'utiliser', 'avantage', 'additifs', 'normes', 'recomendation']
            },
            'lub': {
                'rel': 'lub',
                'cols': ['type', 'utiliser', 'moteurs', 'avantage', 'normes', 'recomendation']
            },
            'batterie': {
                'rel': 'batterie',
                'cols': ['type', 'utiliser', 'moteurs', 'avantage', 'normes', 'recomendation']
            },
            'pneu': {
                'rel': 'pneu',
                'cols': ['type', 'utiliser', 'dimention', 'avantage', 'recomendation']
            },
            'entretien': {
                'rel': 'entretien',
                'cols': ['type', 'utiliser', 'composant', 'avantage', 'instruction', 'recomendation']
            },
            'refroidissement': {
                'rel': 'refroidissement',
                'cols': ['type', 'utiliser', 'moteurs', 'composant', 'norm', 'recomendation']
            },
            'detendeur': {
                'rel': 'detendeur',
                'cols': ['type', 'utiliser', 'compatibilite', 'avantage', 'norm', 'recomendation']
            }
        }

        conf = CONFIG.get(nom_categorie)

        if not conf:
            return "Catégorie invalide", 404

        produits_data = []

        for produit in produits:
            details = getattr(produit, conf['rel'])
            if not details:
                continue

            d = details[0]

            row = {
                'id': produit.id,
                'nom': produit.nom_produit,
                'prix': produit.prix
            }

            for col in conf['cols']:
                row[col] = getattr(d, col, '')

            produits_data.append(row)

        if not produits_data:
            return render_template(
                'user/pro_page.html',
                messege=messege,
                nom_categorie=nom_categorie,
                produits=[],
                prix_min=0,
                prix_max=0,
                prix_max_display=0,
                step=1
            )

        prix_min = min(p['prix'] for p in produits_data)
        prix_max = max(p['prix'] for p in produits_data)
        prix_max_display = prix_max + 1
        step = 1

        return render_template(
            'user/pro_page.html',
            produits=produits_data,
            step=step,
            prix_min=prix_min,
            prix_max=prix_max,
            prix_max_display=prix_max_display,
            cols=conf['cols'],
            nom_categorie=nom_categorie
        )

