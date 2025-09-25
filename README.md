# Test Technique – Startperf

## Auteur
Ray Leonardo VERA

## Contexte
Ce dépôt contient les livrables du **test technique Startperf**.  
Le test est divisé en trois parties :
1. **Exercice 1 – Scrapy Hacker News**  
   Développement d’un spider Scrapy pour récupérer titres, liens et nombre de points des articles de Hacker News.
2. **Exercice 2 – API ScaleSERP**  
   Interrogation de l’API ScaleSERP avec une clé privée afin d’extraire les résultats de recherche Google pour une requête définie.
3. **Exercice 3 – BigQuery / SQL**  
   Création de vues SQL dans Google BigQuery à partir des datasets mis à disposition.

---

## Organisation du dépôt

- Tree repo

    ```bash
    test_technique/
    ├── exercise1/ # Projet Scrapy
    │ ├── exercise1/spiders/hacknewsspider.py
    │ ├── output.json / output.csv
    │ ├── README.md # Doc spécifique Exercice 1
    │ └── scrapy.cfg
    │
    ├── exercise2_scaleserp/ # Script API ScaleSERP
    │ ├── query_scaleserp.py
    │ ├── resultats.json
    │ └── README.md # Doc spécifique Exercice 2
    │
    ├── requirements.txt # Dépendances globales
    └── README.md # Ce fichier (guide général)

---

## Installation

1. Cloner le dépôt et créer un environnement virtuel :
   ```bash
   git clone https://github.com/Leonardo-VERA/test_technique.git
   cd test_technique
   python -m venv .venv
   source .venv/bin/activate

2. Installer les dépendances :

   ```bash
   pip install -r requirements.txt

## Exercice – BigQuery

Les vues SQL ont été créées directement dans le dataset test-vrayleonardo fourni. [BigQuery_project_test](https://console.cloud.google.com/bigquery?project=test-startperf-469408&dataset=test-vrayleonardo)