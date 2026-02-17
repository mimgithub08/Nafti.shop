from sqlalchemy import func
from model import Produit, Categorie

def search_pro(query):
    produits = []
    message = ""
    
    if not query:
        message = "Veuillez entrer un terme de recherche."
        return produits, message, query
    
    # Normaliser la query
    query_lower = query.lower().strip()
    
    # 1. Chercher par ID exact si c'est un nombre
    if query.isdigit():
        produit = Produit.query.get(int(query))
        if produit:
            return [produit], f"Produit trouvé avec l'ID {query}.", query
    
    # 2. Chercher par nom de produit (partiel, case-insensitive)
    produits = Produit.query.filter(
        func.lower(Produit.nom_produit).like(f"%{query_lower}%")
    ).all()
    
    # 3. Si pas de résultats, chercher dans les catégories
    if not produits:
        # Mapping des noms de catégories
        categories_mapping = {
            'carburant': ['carburant', 'essence', 'diesel', 'fuel'],
            'gaz': ['gaz', 'lpg', 'gnv'],
            'lub': ['lub', 'lubrifiant', 'huile', 'oil'],
            'batterie': ['batterie', 'battery', 'accumulateur'],
            'pneu': ['pneu', 'tire', 'pneumatique'],
            'entretien': ['entretien', 'maintenance'],
            'refroidissement': ['refroidissement', 'coolant', 'liquide'],
            'detendeur': ['detendeur', 'détendeur', 'regulator']
        }
        
        # Chercher la catégorie correspondante
        cat_found = None
        for cat_name, keywords in categories_mapping.items():
            if any(keyword in query_lower for keyword in keywords):
                cat_found = cat_name
                break
        
        if cat_found:
            # Récupérer tous les produits en utilisant la relation categorie
            all_produits = Produit.query.all()
            
            for produit in all_produits:
                # Vérifier si le produit a une relation avec la catégorie recherchée
                if hasattr(produit, cat_found):
                    details = getattr(produit, cat_found)
                    if details:
                        produits.append(produit)
            
            if produits:
                return produits, f"{len(produits)} produit(s) trouvé(s) dans la catégorie « {query} ».", query
    
    if produits:
        message = f"{len(produits)} produit(s) trouvé(s) pour « {query} »."
    else:
        message = f"Aucun produit trouvé pour « {query} »."
    
    return produits, message, query