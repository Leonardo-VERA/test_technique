# Exercice 2 – API ScaleSERP

## Objectif
Interroger l’API **ScaleSERP** afin de récupérer les résultats de recherche Google pour la requête **"domino’s pizza"**, en respectant les contraintes suivantes :
- Localisation : Paris, Île-de-France, France  
- Appareil : mobile  
- Page : 1  
- Nombre de résultats par page : 20  

Les résultats doivent être sauvegardés au format JSON sous le nom `resultats.json`.

---

## Pré-requis
- Python 3.9+  
- Compte ScaleSERP et une **API key** valide (à créer via ["app.scaleserp"](https://app.scaleserp.com/signup))

---

## Installation

1. Cloner ce dépôt et créer un environnement virtuel :

   ```bash
   git clone <URL_DU_REPO>
   cd test_technique
   python -m venv .venv
   source .venv/bin/activate

2. Installer les dépendances :
    ```bash
    pip install -r requirements.txt

3. Créer un fichier .env à la racine avec votre clé API :
    ```bash
    SCALESERP_API_KEY="VOTRE_CLE_API_ICI"

---

## Exécution

- Lancer le script :

   cbash
    python exercise2_scaleserp/query_scaleserp.py

- Cela génère un fichier :

    ```bash
    outputs/resultats_scaleserp.json

---

## Vérification
- Les clés principales du JSON sont affichées à l’écran.  
- On peut également vérifier manuellement :

    ```bash
    import json
    data = json.load(open("exercise2_scaleserp/resultats.json", encoding="utf-8"))

    print(data["search_parameters"]["q"])          # "domino's pizza"
    print(data["search_parameters"]["location"])   # "Paris,Paris,Ile-de-France,France"
    print(data["search_parameters"]["device"])     # "mobile"
    print(data["search_parameters"]["num"])        # 20


