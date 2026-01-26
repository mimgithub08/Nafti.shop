from flask import Flask, render_template,request
import os
from sqlalchemy import func, and_
from sqlalchemy import or_
from sqlalchemy.sql.expression import func
from model import db, Produit, Categorie, DetailsCarburant, DetailsGaz, DetailsLub, DetailsBat, DetailsPneu, DetailsEntre, DetailsRefroi, DetailsDet

def init_routes(app):
    
    @app.route('/search', methods=['GET', 'POST'])
    def chercher_du_produits():
        produits = []
        message = ""
        

        query = request.form.get('query', '').strip() if request.method == 'POST' else request.args.get('query', '').strip()
        prix_min = request.args.get('prix_min', type=int)
        prix_max = request.args.get('prix_max', type=int)
        order = request.args.get('order')

        if query:
            produits = Produit.query.filter(
                or_(
                    Produit.nom_produit.ilike(f"%{query}%"),
                    Produit.categorie.ilike(f"%{query}%")
                )
            )

            if prix_min is not None:
                produits = produits.filter(Produit.prix >= prix_min)
            if prix_max is not None:
                produits = produits.filter(Produit.prix <= prix_max)
            if order == 'asc':
                produits = produits.order_by(Produit.prix.asc())
            elif order == 'desc':
                produits = produits.order_by(Produit.prix.desc())

            produits = produits.all()

            if not produits:
                message = f"Aucun produit trouvé pour « {query} »."

        return render_template('user/result.html', produits=produits, message=message)


    @app.route('/')
    def homepage():
        produits_aleatoires = Produit.query.order_by(func.random()).limit(18).all()
        photos= ['slider.png','sliderindex.png']
        return render_template('user/index.html',produits=produits_aleatoires ,photos=photos)

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

    @app.route('/filtrer_ajax')
    def filtrer_ajax():
        categorie = request.args.get('cate_id')
        prix_min = request.args.get('prix_min', type=int)
        prix_max = request.args.get('prix_max', type=int)
        order = request.args.get('order')  

        query = Produit.query.filter(
            and_(
                Produit.categorie == categorie,
                Produit.prix >= prix_min,
                Produit.prix <= prix_max
            )
        )

        if order == 'asc':
            query = query.order_by(Produit.prix.asc())
        elif order == 'desc':
            query = query.order_by(Produit.prix.desc())

        produits = query.all()

        return render_template('user/card.html', produits=produits)


    @app.route('/categorie/<int:cate_id>')
    def produit_cat(cate_id):

        cat = Categorie.query.get(cate_id)
        if not cat:
            return "Catégorie non trouvée", 404

        produits = Produit.query.filter_by(cat_num=cat.id).all()
        nombre_produits = len(produits)

        if nombre_produits > 0:
            prix_min = db.session.query(func.min(Produit.prix)).filter_by(cat_num=cat.id).scalar()
            prix_max = db.session.query(func.max(Produit.prix)).filter_by(cat_num=cat.id).scalar()
            prix_max_display = prix_max + 1
            step = 1
        else:
            prix_min = prix_max = prix_max_display = 0
            step = 1

        return render_template(
            'user/pro_page.html',
            produits=produits,
            step=step,
            prix_min=prix_min,
            prix_max=prix_max,
            prix_max_display=prix_max_display,
            categorie=cat.name
        )
