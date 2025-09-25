# Exercice 1 – Scrapy Hacker News

## Objectif

Utiliser Scrapy afin de récupérer les titres, liens et scores des articles présents sur la page d’accueil de Hacker News [lien](https://news.ycombinator.com/)

L’objectif est d’extraire les données, de les sauvegarder au format JSON ou CSV, et de gérer la pagination pour collecter plusieurs pages.

---

## Pré-requis

- Python 3.9+  
- Environnement virtuel avec Scrapy installé  


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

---
## Structure du projet
Le projet Scrapy est situé dans le dossier exercise1/ :
    ```bash
    exercise1/
    ├── exercise1/
    │   ├── settings.py
    │   ├── spiders/
    │   │   └── hacknewsspider.py   # Spider principal
    │   └── ...
    ├── output.json                 # Résultats en JSON
    ├── output.csv                  # Résultats en CSV
    └── scrapy.cfg

## Exécution

1. Se placer dans le dossier racine du projet :

    ```bash
    cd exercise1

2. Lancer le spider et sauvegarder les résultats au format JSON :

    ```bash
    scrapy crawl hacknews -O outputs/output.json # .json
    scrapy crawl hacknews -O outputs/output.csv # .csv

Le spider va automatiquement parcourir plusieurs pages grâce au bouton More.

---

## Exemple de sortie  
1. 

    ```bash
    {
        "title": "Snapdragon X2 Elite ARM Laptop CPU",
        "link": "https://www.qualcomm.com/products/mobile/snapdragon/laptops-and-tablets/snapdragon-x2-elite",
        "score": "37 points"
    }

## Vérification
- Les fichiers générés (output.json ou output.csv) peuvent être ouverts avec un éditeur de texte, Excel, ou bien directement en Python :

    ```bash
    import pandas as pd
    df = pd.read_csv("exercise1/output.csv")
    print(df.head())

