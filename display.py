from model import db, Produit, Categorie, DetailsCarburant, DetailsGaz, DetailsLub, DetailsBat, DetailsPneu, DetailsEntre, DetailsRefroi, DetailsDet

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

def get_produits_by_categorie(nom_categorie):
    conf = CONFIG.get(nom_categorie)
    if not conf:
        return [], None

    produits = Produit.query.all()
    produits_data = []

    for produit in produits:
        # نجيب relation حسب config
        details = getattr(produit, conf['rel'], None)

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

    # 👇 هنا التغيير المهم
    return produits_data, nom_categorie
